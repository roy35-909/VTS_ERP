from rest_framework import serializers
from user.models import User
from . models import *
from user.serializers import *


class MeetingSerializer(serializers.ModelSerializer):
    meet_attender = UserSerializer(many=True)

    class Meta:
        model = Meeting
        fields = '__all__'




