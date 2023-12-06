
from django.urls import path
from .views import *
urlpatterns = [
    path('create_employee', EmployeeViews.as_view()),
    path('edit_employee/<int:pk>', EditEmployee.as_view()),
    path('edit_employee_profile_user',EditEmployeeProfileUser.as_view()),
    path('create_client',ClientViews.as_view()),
    path('edit_client/<int:pk>',EditClient.as_view()),
    path('edit_client_profile_user',EditClientProfileUser.as_view()),

]
