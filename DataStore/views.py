from django.contrib import messages
from django.shortcuts import redirect, render
from . models import onefitTabel
def home(request):
    return render(request, 'index.html')

def result(request):
    list_of_peoples = onefitTabel.objects.all().order_by('-number_of_days')
    count, n, user_det, search, user = 1, 0, 0, 0, None
    for user in list_of_peoples:
        if(int(user.total_calories_burned) >= 0):
            user.rank = count
            user.save()
            count += 1
    top_10_place = onefitTabel.objects.all().order_by('rank')
   
    if request.method == "POST":
        l = onefitTabel.objects.filter(user_id = request.POST['username'])
        search = 1
        if(len(l) == 0):
            n = 1
        else:
            user_det = 1
            user = l[0] 
    context = {
        'top_10_place': top_10_place,
        'user_det':user_det,
        'user':user,
        'n':n,
    }
    return render(request, 'results.html', context)

def update_calories(request):
    if request.method == "POST":
        id = onefitTabel.objects.filter(user_id = request.POST['id'])
        if(len(id) == 1):
            id[0].total_calories_burned = int(id[0].total_calories_burned) + int(request.POST['calories'])
            id[0].save()
            messages.success(request, "Calories Updated Suceefully.")
            return redirect('update_calories')
        elif(len(id) == 0):
            messages.info(request, "OneFit Id Can't be found!!")
            return redirect('update_calories')   
    return render(request, 'update_calories.html')