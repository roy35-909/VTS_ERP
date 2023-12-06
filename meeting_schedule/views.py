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



class MeetingAPIview(APIView):

    def get(self, request):

        meetings = Meeting.objects.all()

        ser = MeetingSerializer(meetings,many = True, context={'request':request})

        return Response(ser.data, status=status.HTTP_200_OK)
    

    def post(self, request):

        data = request.data 

        if 'meet_title' not in data:
            return Response({'error':'Meet Title not porvided'},status=status.HTTP_406_NOT_ACCEPTABLE)
        
        if 'meet_link' not in data:
            return Response({'error':'Meet lInk not provided'},status=status.HTTP_406_NOT_ACCEPTABLE)
        
        if 'meet_time' not in data:

            return Response({'error': 'Please Provide Meet Time '},status=status.HTTP_406_NOT_ACCEPTABLE)
        
        meeting = Meeting.objects.create(meet_title = data['meet_title'], meet_link = data['meet_link'], meet_time = data['meet_time'])

        if  'meet_docs' in data:
            meeting.meet_docs = request.FILES['meet_docs']
        
        if 'meet_detatils' in data:
            meeting.meet_detatils = data['meet_detatils']

        if 'meet_attender' in data:
# Need To Debug Here.......
            for i in data['meet_attender']:
                try:
                    user = User.objects.get(id = i)
                except(ObjectDoesNotExist):
                    return Response({'error':'User Not Found'}, status=status.HTTP_404_NOT_FOUND)
                
                # except:
                #     return Response({'error':'Something Went Wrong in Meeting API View'},status=status.HTTP_400_BAD_REQUEST)
                
                meeting.meet_attender.add(user)

        meeting.save()

        return self.get(request)
    

class EditMeeting(APIView):

    def get(self,request,pk):

        try:
            meeting = Meeting.objects.get(id=pk)
        except(ObjectDoesNotExist):

            return Response({'error':'Service Not Found In Databases'},status=status.HTTP_404_NOT_FOUND)
        
        #Make a Except In Deployment
        # except:
        #     return Response({'error':'Something is Wrong...'},status=status.HTTP_400_BAD_REQUEST)

        ser = MeetingSerializer(meeting,context = {'request':request})

        return Response(ser.data, status=status.HTTP_200_OK)
    

    def put(self,request,pk):

        try:
            meeting = Meeting.objects.get(id=pk)
        except(ObjectDoesNotExist):

            return Response({'error':'Service Not Found In Databases'},status=status.HTTP_404_NOT_FOUND)
        
        #Make a Except In Deployment
        # except:
        #     return Response({'error':'Something is Wrong...'},status=status.HTTP_400_BAD_REQUEST)
        data = request.data 
        if 'meet_title' in data:

            meeting.meet_title = data['meet_title']
        
        if 'meet_link' in data:
            meeting.meet_link = data['meet_link']

        if 'meet_docs' in data:
            meeting.meet_docs = data['meet_docs']
        if 'meet_time' in data:
            meeting.meet_time = data['meet_time']

        if 'meet_attender' in data:
# Need To Debug Here.......
            for i in data['meet_attender']:
                try:
                    user = User.objects.get(id = i)
                except(ObjectDoesNotExist):
                    return Response({'error':'User Not Found'}, status=status.HTTP_404_NOT_FOUND)
                
                # except:
                #     return Response({'error':'Something Went Wrong in Meeting API View'},status=status.HTTP_400_BAD_REQUEST)
                
                meeting.meet_attender.add(user)

        meeting.save()

        return self.get(request=request,pk=pk)
    

    def delete(self,request,pk):


        try:
            meeting = Meeting.objects.get(id=pk)
        except(ObjectDoesNotExist):

            return Response({'error':'Service Not Found In Databases'},status=status.HTTP_404_NOT_FOUND)
        
        #Make a Except In Deployment
        # except:
        #     return Response({'error':'Something is Wrong...'},status=status.HTTP_400_BAD_REQUEST)

        meeting.delete()

        return MeetingAPIview.get(self=self,request=request,pk=pk)