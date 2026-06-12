from django.urls import path
from .views import register,login_,logout_,profile,reset_pasw

urlpatterns = [
    path('register/', register, name='register'),
    path('login_/', login_, name='login_'),
    path('logout_/', logout_, name='logout_'),
    path('profile/', profile, name='profile'),
    path('reset_pasw/', reset_pasw, name='reset_pasw'),

]