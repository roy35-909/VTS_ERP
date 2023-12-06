from django.urls import path
from .views import *
urlpatterns = [

    path('create_meeting',MeetingAPIview.as_view()),
    path('edit_meeting/<int:pk>',EditMeeting.as_view()),
]