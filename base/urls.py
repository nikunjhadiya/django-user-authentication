from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('trash/',trash,name='trash'),
    path('delete/<int:id>/',delete,name='delete'),
    path('trestore/<int:pk>/',trestore,name='trestore'),
    path('deleteall/',deleteall,name = 'deleteall'),
    path('trestoreall/',trestoreall,name = 'trestoreall'),
    path('tdeleteall/', tdeleteall, name='tdeleteall'),
    path('tdelete/<int:pk>/', tdelete, name='tdelete'),

]