from django.urls import path
from .views import register,login_,logout_,profile,reset_pasw,forget_pasw,update,about,change_image

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_, name='login_'),
    path('logout/', logout_, name='logout_'),
    path('profile/', profile, name='profile'),
    path('reset_pasw/', reset_pasw, name='reset_pasw'),
    path('forget_pasw/', forget_pasw, name='forget_pasw'),
    path('update/', update, name='update'),
    path('about/', about, name='about'),
    path('change_image/', change_image, name='change_image'),
]