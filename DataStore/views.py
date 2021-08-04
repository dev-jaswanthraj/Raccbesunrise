from django.shortcuts import render
from . models import onefitTabel
def home(request):
    return render(request, 'index.html')

def result(request):
    list_of_peoples = onefitTabel.objects.all().order_by('-total_calories_burned').order_by('-number_of_days')
    count, n, user_det = 1, 0, 0
    for user in list_of_peoples:
        if(int(user.total_calories_burned) > 0):
            user.rank = count
            user.save()
            count += 1
    top_10_place = onefitTabel.objects.all().order_by('rank')[0:11]
   
    if request.method == "POST":
        l = onefitTabel.objects.filter(user_id = request.POST['username'])
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