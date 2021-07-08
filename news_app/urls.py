from django.urls import path
from . import views

urlpatterns =[
    path("home",views.home,name='home'),
    path("",views.home,name='home'),
    path("sports",views.sports,name='sports'),
    path("entertainment",views.ent,name='entertainment'),
    path("health",views.health,name='health'),
    path("business",views.business,name='business'),
    path("tech",views.tech,name='tech'),
]