from django.urls import path
from .views import *
urlpatterns = [

    path('create_services',ServiceAPIview.as_view()),
    path('edit_services/<int:pk>',EditServiceAPIview.as_view()),
    path('create_review',ReviewAPIview.as_view()),
    path('edit_review/<int:pk>',EditReviewAPIview.as_view()),

]