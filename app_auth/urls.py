
from django.urls import path
from app_auth import views

urlpatterns = [
    path('', views.Register, name='register'),
    path('home/',views.Home_Page,name='home'),
    path('login/',views.Login, name ='login'),
    path('register/',  views.Register,name='register'),
    path('logout/',views.logout_user,name='logout'),

]