from rest_framework import serializers
from user.models import User
from . models import *
from user.serializers import *


class ReviewSerializer(serializers.ModelSerializer):


    class Meta:
        model = Review
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):

    review = serializers.SerializerMethodField()
    class Meta:
        model = Service
        fields = '__all__'

    def get_review(self,instance):

        r = Review.objects.filter(service = instance)
        ser = ReviewSerializer(r,many = True)
        return ser.data



