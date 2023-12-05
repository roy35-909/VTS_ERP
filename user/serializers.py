from rest_framework import serializers
from user.models import User
from . models import *


class EmployeeProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        exclude = ('user',)


class ClientProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        exclude = ('user',)



class AdminProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Admin
        exclude = ('user',)


class UserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('id','username','email','first_name','last_name','dateEnrolled','Type','profile')
        
    def get_profile(self,instance):

        if instance.Type=="Admin":
            profile = Admin.objects.get(user=instance)
            profile_ser = AdminProfileSerializer(profile)
            return profile_ser.data
      
        elif instance.Type=="Employee":
            profile = Employee.objects.get(user=instance)
            profile_ser = EmployeeProfileSerializer(profile, context={'request' : self.context.get('request')})
            return profile_ser.data
      
        elif instance.Type=="Client":
            profile = Client.objects.get(user=instance)
            profile_ser = ClientProfileSerializer(profile)
            return profile_ser.data
        
        else:
            return None
