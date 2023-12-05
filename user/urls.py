
from django.urls import path
from .views import *
urlpatterns = [
    path('create_employee', EmployeeViews.as_view()),
    path('edit_employee/<int:pk>', EditEmployee.as_view()),

]
