from django.urls import path
from .views import *
urlpatterns = [

path('create_project_type',ProjectTypeAPIview.as_view()),
path('create_project_type/<int:pk>',EditProjectAPIview.as_view()),

path('create_project',ProjectAPIview.as_view()),
path('create_project/<int:pk>',EditProjectAPIview.as_view()),

]