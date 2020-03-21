from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('test/',views.test, name='test'),
    path('base/',views.base, name='base'),
    path('add',views.add, name='add'),
    path('add2',views.add2, name='add2'),
]
