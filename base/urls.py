from django.urls import path
from . import views

urlpatterns = [
    path('', views.endpoints),
    path('schools/', views.schools),
    path('school/<str:username>', views.school), # function-based views
    #path('schools/<str:username>', views.SchoolDetail.as_view()),  Class=based views

   
]