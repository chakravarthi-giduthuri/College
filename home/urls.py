
from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('create/', Create, name='create'),
    path('post/<int:pk>/', Post, name='post'),
    path('update/<int:pk>/', Update, name='update'),
    path('delete/<int:pk>/', Delete, name='delete')

]



