from rest_framework import serializers
from user.models import User
from . models import *
from user.serializers import *

class ProjectTypeSerializer(serializers.ModelSerializer):
    created_by = UserSerializer()
    class Meta:
        model = ProjectType
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    developer = EmployeeProfileSerializer(many=True)
    project_owner = ClientProfileSerializer()
    ProjectType = ProjectTypeSerializer()
    created_by = UserSerializer()
    class Meta:
        model = Project
        fields = '__all__'
