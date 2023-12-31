from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from django.contrib.auth import update_session_auth_hash
from .models import *
from .serializers import *


class EmployeeViews(APIView):

    serializers = UserSerializer
    permission_classes = []
    def get(self,request):
        employees = User.objects.filter(Type = "Employee")

        employees_ser = UserSerializer(employees, many=True, context={'request':request})

        return Response(employees_ser.data, status=status.HTTP_200_OK)
    

    def post(self,request):

        data = request.data 

        if 'email' not in data:
            return Response({"error":"Please Provide Email."},status=status.HTTP_406_NOT_ACCEPTABLE)
        if 'password' not in data:
            return Response({"error":"Please Provide Password"},status=status.HTTP_406_NOT_ACCEPTABLE)
        if 'username' not in data:
            username = data['email'].split('@')
            username = username[0]

        else:
            username = data['username']

        user = User.objects.create(username = username, email=data['email'], Type='Employee')
        user.set_password(data['password'])

        if 'first_name' in data:
            user.first_name = data['first_name']
        if 'last_name' in data:
            user.last_name = data['last_name']
        user.save()

        profile = Employee.objects.create(user=user)

        if 'dob' in data:
            profile.dob = data['dob']

        if 'phone' in data:
            profile.phone = data['phone']

        if 'github' in data:
            profile.github = data['github']

        if 'linkedin' in data:
            profile.linkedin = data['linkedin']

        if 'facebook' in data:
            profile.facebook = data['facebook']

        if 'photo' in data:
            profile.photo = request.FILES['photo']

        profile.save()

        return self.get(request)
    


    



class EditEmployee(APIView):

    serializers = UserSerializer
    permission_classes = []


    def put(self,request,pk):
        data= request.data

        try:
            user = User.objects.get(id=pk)
        except(ObjectDoesNotExist):
            return Response({"error":"Object Does Not Exist . "},status = status.HTTP_404_NOT_FOUND)




        if user.Type != 'Employee':
            return Response({'error':'User not a Employee..'},status=status.HTTP_406_NOT_ACCEPTABLE)
        

        if 'password' in data:
            user.set_password(data['password'])

        if 'first_name' in data:
            user.first_name = data['first_name']
        if 'last_name' in data:
            user.last_name = data['last_name']

        user.save()

        profile = Employee.objects.get(user=user)

        if 'dob' in data:
            profile.dob = data['dob']

        if 'phone' in data:
            profile.phone = data['phone']

        if 'github' in data:
            profile.github = data['github']

        if 'linkedin' in data:
            profile.linkedin = data['linkedin']

        if 'facebook' in data:
            profile.facebook = data['facebook']

        if 'photo' in data:
            profile.photo = request.FILES['photo']

        profile.save()
        ser = UserSerializer(user,context={'request':request})
        return Response(ser.data,status=status.HTTP_201_CREATED)
    
    def get(self,request,pk):
        try:
            user = User.objects.get(id=pk)
        except(ObjectDoesNotExist):
            return Response({"error":"Object Does Not Exist . "},status = status.HTTP_404_NOT_FOUND)
        
        if user.Type != 'Employee':
            return Response({'error':'User not a Employee..'},status=status.HTTP_406_NOT_ACCEPTABLE)
        
        ser = UserSerializer(user, context={'request':request})
        return Response(ser.data, status=status.HTTP_200_OK)
    

    def delete(self,request,pk):
        try:
            user = User.objects.get(id=pk)

        except(ObjectDoesNotExist):
            return Response({"error":"Object Does Not Exist . "},status = status.HTTP_404_NOT_FOUND)
        
        if user.Type != 'Employee':
            return Response({'error':'User not a Employee..'},status=status.HTTP_406_NOT_ACCEPTABLE)
        
        user.delete()

        return EmployeeViews.get(self=self,request=request)



class EditEmployeeProfileUser(APIView):

    permission_classes=[]
    def get(self,request):
        user = request.user
        if user.Type!='Employee':
            return Response({'error':'Please Hit on Employee Edit Profile Endpoints'},status=status.HTTP_404_NOT_FOUND)
        
        profile = Employee.objects.get(user=user)
        ser = UserSerializer(user,context={'request':request})
        return Response(ser.data,status=status.HTTP_200_OK)
    
    def put(self,request):
        data= request.data
        user = request.user

        if user.Type != 'Employee':
            return Response({'error':'User not a Employee..'},status=status.HTTP_404_NOT_FOUND)
        

        if 'password' in data:
            user.set_password(data['password'])

        if 'first_name' in data:
            user.first_name = data['first_name']
        if 'last_name' in data:
            user.last_name = data['last_name']

        user.save()

        try:
            profile = Employee.objects.get(user=user)
        except(ObjectDoesNotExist):
            return Response({'error':'Profile Not Found Fot this Employee'}, status=status.HTTP_404_NOT_FOUND)

        if 'dob' in data:
            profile.dob = data['dob']

        if 'phone' in data:
            profile.phone = data['phone']

        if 'github' in data:
            profile.github = data['github']

        if 'linkedin' in data:
            profile.linkedin = data['linkedin']

        if 'facebook' in data:
            profile.facebook = data['facebook']

        if 'photo' in data:
            profile.photo = request.FILES['photo']

        profile.save()
        ser = UserSerializer(user,context={'request':request})
        return Response(ser.data,status=status.HTTP_201_CREATED)




class ClientViews(APIView):

    serializers = UserSerializer
    permission_classes = []
    def get(self,request):
        client = User.objects.filter(Type = "Client")

        client_ser = UserSerializer(client, many=True, context={'request':request})

        return Response(client_ser.data, status=status.HTTP_200_OK)
    

    def post(self,request):

        data = request.data 

        if 'email' not in data:
            return Response({"error":"Please Provide Email."},status=status.HTTP_406_NOT_ACCEPTABLE)
        if 'password' not in data:
            return Response({"error":"Please Provide Password"},status=status.HTTP_406_NOT_ACCEPTABLE)
        if 'username' not in data:
            username = data['email'].split('@')
            username = username[0]

        else:
            username = data['username']

        user = User.objects.create(username = username, email=data['email'], Type='Client')
        user.set_password(data['password'])

        if 'first_name' in data:
            user.first_name = data['first_name']
        if 'last_name' in data:
            user.last_name = data['last_name']
        user.save()

        profile = Client.objects.create(user=user)

        if 'dob' in data:
            profile.dob = data['dob']

        if 'phone' in data:
            profile.phone = data['phone']

        if 'github' in data:
            profile.github = data['github']

        if 'linkedin' in data:
            profile.linkedin = data['linkedin']

        if 'facebook' in data:
            profile.facebook = data['facebook']

        if 'photo' in data:
            profile.photo = request.FILES['photo']

        profile.save()

        return self.get(request)



class EditClient(APIView):

    serializers = UserSerializer
    permission_classes = []


    def put(self,request,pk):
        data= request.data

        try:
            user = User.objects.get(id=pk)
        except(ObjectDoesNotExist):
            return Response({"error":"Object Does Not Exist . "},status = status.HTTP_404_NOT_FOUND)




        if user.Type != 'Client':
            return Response({'error':'User not a Client..'},status=status.HTTP_406_NOT_ACCEPTABLE)
        

        if 'password' in data:
            user.set_password(data['password'])

        if 'first_name' in data:
            user.first_name = data['first_name']
        if 'last_name' in data:
            user.last_name = data['last_name']

        user.save()

        try:
            profile = Client.objects.get(user=user)
        except(ObjectDoesNotExist):
            return Response({'error':'Client Profile fot this Client Does not Exist..'}, status=status.HTTP_404_NOT_FOUND)
        

        if 'dob' in data:
            profile.dob = data['dob']

        if 'phone' in data:
            profile.phone = data['phone']

        if 'github' in data:
            profile.github = data['github']

        if 'linkedin' in data:
            profile.linkedin = data['linkedin']

        if 'facebook' in data:
            profile.facebook = data['facebook']

        if 'photo' in data:
            profile.photo = request.FILES['photo']

        profile.save()
        ser = UserSerializer(user,context={'request':request})
        return Response(ser.data,status=status.HTTP_201_CREATED)
    
    def get(self,request,pk):
        try:
            user = User.objects.get(id=pk)
        except(ObjectDoesNotExist):
            return Response({"error":"Object Does Not Exist . "},status = status.HTTP_404_NOT_FOUND)
        
        if user.Type != 'Client':
            return Response({'error':'User not a Client..'},status=status.HTTP_406_NOT_ACCEPTABLE)
        
        ser = UserSerializer(user, context={'request':request})
        return Response(ser.data, status=status.HTTP_200_OK)
    

    def delete(self,request,pk):
        try:
            user = User.objects.get(id=pk)

        except(ObjectDoesNotExist):
            return Response({"error":"Object Does Not Exist . "},status = status.HTTP_404_NOT_FOUND)
        
        if user.Type != 'Client':
            return Response({'error':'User not a Client..'},status=status.HTTP_406_NOT_ACCEPTABLE)
        
        user.delete()

        return ClientViews.get(self=self,request=request)




class EditClientProfileUser(APIView):

    permission_classes=[]
    def get(self,request):
        user = request.user
        if user.Type!='Client':
            return Response({'error':'Please Hit on Client Edit Profile Endpoints'},status=status.HTTP_404_NOT_FOUND)
        
        try:
            profile = Client.objects.get(user=user)
        except(ObjectDoesNotExist):
            return Response({'error':'Client Profile Not Found In Database..'},status=status.HTTP_404_NOT_FOUND)
        
        ser = UserSerializer(user,context={'request':request})
        return Response(ser.data,status=status.HTTP_200_OK)
    
    def put(self,request):
        data= request.data
        user = request.user

        if user.Type != 'Client':
            return Response({'error':'User not a Client..'},status=status.HTTP_404_NOT_FOUND)
        

        if 'password' in data:
            user.set_password(data['password'])

        if 'first_name' in data:
            user.first_name = data['first_name']
        if 'last_name' in data:
            user.last_name = data['last_name']

        user.save()

        try:
            profile = Client.objects.get(user=user)
        except(ObjectDoesNotExist):
            return Response({'error':'Profile Not Found Fot this Client'}, status=status.HTTP_404_NOT_FOUND)

        if 'dob' in data:
            profile.dob = data['dob']

        if 'phone' in data:
            profile.phone = data['phone']

        if 'github' in data:
            profile.github = data['github']

        if 'linkedin' in data:
            profile.linkedin = data['linkedin']

        if 'facebook' in data:
            profile.facebook = data['facebook']

        if 'photo' in data:
            profile.photo = request.FILES['photo']

        profile.save()
        ser = UserSerializer(user,context={'request':request})
        return Response(ser.data,status=status.HTTP_201_CREATED)