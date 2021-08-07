from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

class onefitTabel(models.Model):
    user_id = models.CharField(unique= True, max_length=200)
    user_name = models.CharField(max_length=200, null = True, blank= True)
    total_calories_burned = models.IntegerField(default=0, blank=True, null=True)
    number_of_days = models.IntegerField(default=0, blank=True, null=True)
    rank = models.CharField(default= None , max_length = 6)

    def __str__(self):
        return self.user_id

@receiver(pre_save, sender=onefitTabel)
def update_stock(sender, instance, **kwargs):
    if len(onefitTabel.objects.filter(id = instance.id)) == 1:
        if(onefitTabel.objects.get(id = instance.id).total_calories_burned !=  instance.total_calories_burned):
            instance.number_of_days = str(int(instance.number_of_days)+1)
            pre_save.disconnect(update_stock, sender=onefitTabel)
            instance.save()
            pre_save.connect(update_stock, sender=onefitTabel)