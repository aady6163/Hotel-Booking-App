
from django.urls import path
from .views import *

urlpatterns = [
    path('' , home , name="home"),
    path('login/' , login_page , name="login"),
    path('logout/' , logout_page , name="logout"),
    path('register/' , register_page , name="register"),
    path('hotel_detail/<uid>' , hotel_detail , name="hotel_detail"),
]
