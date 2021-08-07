from . views import home, result, update_calories
from django.urls import path

urlpatterns = [
    path('', home, name= "home"),
    path('results/', result, name='results'),
    path('update/', update_calories, name='update_calories')
]