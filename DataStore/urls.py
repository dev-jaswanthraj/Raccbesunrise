from . views import home, result
from django.urls import path

urlpatterns = [
    path('', home, name= "home"),
    path('results/', result, name='results')
]