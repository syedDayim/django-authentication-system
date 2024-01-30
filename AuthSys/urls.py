from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', user_signup, name='signup'),
    path('profile/', user_profile, name='profile'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('change_password/', user_change_password, name='change_password'),
    path('change_password_wo/', user_change_password_wo, name='change_password_wo'),
]
