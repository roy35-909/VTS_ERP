from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from django.contrib.auth import update_session_auth_hash
from .models import *
from .serializers import *
from user.models import *
import json




class ServiceAPIview(APIView):

    def get(self,request):

        services = Service.objects.all()
        ser = ServiceSerializer(services,many=True, context = {'request':request})

        return Response(ser.data,status=status.HTTP_200_OK)
   

    def post(self,request):


        data = request.data 

        if 'name' not in data:

            return Response({'error':'Please Provide name'},status=status.HTTP_406_NOT_ACCEPTABLE)
        if 'details' not in data:
            return Response({'error':'Please Provide Details'},status=status.HTTP_406_NOT_ACCEPTABLE)

        service = Service.objects.create(name = data['name'], details = data['details'])

        if 'amount_of_service' in data:
            service.amount_of_service = data['amount_of_service']
        
        if 'photo' in data:
            service.photo = request.FILES['photo']
        service.save()

        return self.get(request)
    


class EditServiceAPIview(APIView):

    def get(self,request,pk):

        try:
            service = Service.objects.get(id=pk)
        except(ObjectDoesNotExist):

            return Response({'error':'Service Not Found In Databases'},status=status.HTTP_404_NOT_FOUND)
        
        #Make a Except In Deployment
        # except:
        #     return Response({'error':'Something is Wrong...'},status=status.HTTP_400_BAD_REQUEST)

        ser = ServiceSerializer(service,context = {'request':request})

        return Response(ser.data, status=status.HTTP_200_OK)
    

    def put(self,request,pk):

        try:
            service = Service.objects.get(id=pk)
        except(ObjectDoesNotExist):

            return Response({'error':'Service Not Found In Databases'},status=status.HTTP_404_NOT_FOUND)
        
        #Make a Except In Deployment
        # except:
        #     return Response({'error':'Something is Wrong...'},status=status.HTTP_400_BAD_REQUEST)
        
        data = request.data

        if 'name' in data:

            service.name = data['name']

        if 'photo' in data:
            service.photo = request.FILES['photo']
        
        if 'details' in data:
            service.details = data['details']

        if 'amount_of_service' in data:
            service.amount_of_service = data['amount_of_service']

        service.save()

        return self.get(self=self,request=request,pk=pk)
    

    def delete(self,request,pk):
        try:
            service = Service.objects.get(id=pk)
        except(ObjectDoesNotExist):

            return Response({'error':'Service Not Found In Databases'},status=status.HTTP_404_NOT_FOUND)
        
        #Make a Except In Deployment
        # except:
        #     return Response({'error':'Something is Wrong...'},status=status.HTTP_400_BAD_REQUEST)


        service.delete()

        return ServiceAPIview.get(self=self,request=request)
    



class ReviewAPIview(APIView):

    def get(self,request):

        review = Review.objects.all()

        ser = ReviewSerializer(review,many = True, context={'request':request})

        return Response(ser.data, status=status.HTTP_200_OK)
    

    def post(self,request):

        data = request.data 

        if 'client' not in data:
            if request.user.Type != 'Client':
                return Response({'error':'Please Provide Client'},status=status.HTTP_406_NOT_ACCEPTABLE)
            
            else:

                try:
                    client = Client.objects.get(user=request.user)
                except(ObjectDoesNotExist):
                    return Response({'error':'Please Provide Client'},status=status.HTTP_406_NOT_ACCEPTABLE)
                # except:
                #     return Response({'error':'Something Went Wrong'},status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                client = Client.objects.get(id=data['client'])
            except(ObjectDoesNotExist):
                return Response({'error':'Client Not Found'},status=status.HTTP_404_NOT_FOUND)
            
            # Make a Except in Deployment

            # except:
            #     return Response({'error':'Something Went Wrong'},status=status.HTTP_400_BAD_REQUEST)


        if 'service' not in data:

            return Response({'error':'Please provide Service id'},status=status.HTTP_406_NOT_ACCEPTABLE)
        
        if 'review' not in data:

            return Response({'error':'Please Provide review...'},status=status.HTTP_406_NOT_ACCEPTABLE)
        
        try:
            service = Service.objects.get(id=data['service'])

        except(ObjectDoesNotExist):
            return Response({'error':'Service Not Found '},status=status.HTTP_404_NOT_FOUND)
        
        # Make a Except in Deployment
        # except:
        #     return Response({'error':'Something Went Wrong'},status=status.HTTP_400_BAD_REQUEST)
        

        review = Review.objects.create(client = client,service = service, review = data['review'])

        review.save()

        return self.get(request)
    


class EditReviewAPIview(APIView):

    def get(self,request,pk):

        try:
            review = Review.objects.get(id=pk)
        except(ObjectDoesNotExist):

            return Response({'error':'Review Not Found In Databases'},status=status.HTTP_404_NOT_FOUND)
        
        #Make a Except In Deployment
        # except:
        #     return Response({'error':'Something is Wrong...'},status=status.HTTP_400_BAD_REQUEST)

        ser = ReviewSerializer(review,context = {'request':request})

        return Response(ser.data, status=status.HTTP_200_OK)
    

    def put(self,request,pk):

        try:
            review = Review.objects.get(id=pk)
        except(ObjectDoesNotExist):

            return Response({'error':'Review Not Found In Databases'},status=status.HTTP_404_NOT_FOUND)
        
        #Make a Except In Deployment
        # except:
        #     return Response({'error':'Something is Wrong...'},status=status.HTTP_400_BAD_REQUEST)


        data = request.data 
        if 'review' in data:
            review.review = data['review']


        review.save()

        return self.get(self=self,request=request,pk=pk)
    

    def delete(self,request,pk):

        try:
            review = Review.objects.get(id=pk)
        except(ObjectDoesNotExist):

            return Response({'error':'Review Not Found In Databases'},status=status.HTTP_404_NOT_FOUND)
        
        #Make a Except In Deployment
        # except:
        #     return Response({'error':'Something is Wrong...'},status=status.HTTP_400_BAD_REQUEST)


        review.delete()

        return ReviewAPIview.get(self=self,request=request)
    