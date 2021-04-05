from django.urls import path
from .views import studentRegister, register, teacherRegister, loginPage, logoutPage

urlpatterns = [
    path('register/', register, name='register'),
    path('student', studentRegister, name='student'),
    path('teacher/', teacherRegister, name='teacher'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutPage, name='logout')
]
