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

class ProjectTypeAPIview(APIView):

    permission_classes = [IsAdminUser]

    def get(self,request):

        types = ProjectType.objects.all()

        ser = ProjectTypeSerializer(types,many=True, context = {'request':request})
        return Response(ser.data, status=status.HTTP_200_OK)
    

    def post(self,request):

        data = request.data 

        if 'name' not in data:
            return Response({"error":"Please provide name"},status=status.HTTP_406_NOT_ACCEPTABLE)
        
        if 'thumbline' not in data:
            return Response({"error":"Please provide thumbline"},status=status.HTTP_406_NOT_ACCEPTABLE)
        
        types = ProjectType.objects.create(name = data['name'],thumbline = data['thumbline'],created_by=request.user)

        types.save()

        return self.get(request)
    

class EditProjectTypeAPIview(APIView):

    def get(self,request,pk):

        try:
            types = ProjectType.objects.get(id=pk)

        except(ObjectDoesNotExist):
            return Response({'error':'Projects Type Not Found in Database'},status=status.HTTP_404_NOT_FOUND)
        
        except:
            return Response({'error':'Please your primanry key datatype and try again..'},status=status.HTTP_400_BAD_REQUEST)
        
        ser = ProjectTypeSerializer(types,context={'request':request})

        return Response(ser.data, status=status.HTTP_200_OK)

    
    def put(self,request,pk):

        data = request.data
        try:
            types = ProjectType.objects.get(id=pk)

        except(ObjectDoesNotExist):
            return Response({'error':'Projects Type Not Found in Database'},status=status.HTTP_404_NOT_FOUND)
        
        except:
            return Response({'error':'Please your primanry key datatype and try again..'},status=status.HTTP_400_BAD_REQUEST)
        
        if 'name' in data:

            types.name = data['name']
        if 'thumbline' in data:

            types.thumbline = data['thumbline']

        types.save()

        return self.get(self=self,request=request,pk=pk)


    def delete(self,request,pk):

        try:
            types = ProjectType.objects.get(id=pk)

        except(ObjectDoesNotExist):
            return Response({'error':'Projects Type Not Found in Database'},status=status.HTTP_404_NOT_FOUND)
        
        except:
            return Response({'error':'Please your primanry key datatype and try again..'},status=status.HTTP_400_BAD_REQUEST)
        

        types.delete()

        return ProjectTypeAPIview.get(self=self,request=request)
    

class ProjectAPIview(APIView):

    permission_classes=[]
    

    def get(self,request):

        projects = Project.objects.all()

        ser = ProjectSerializer(projects,many=True,context={'request':request})

        return Response(ser.data,status=status.HTTP_200_OK)
    

    # Create A Projects....

    def post(self,request):

        data = request.data 


        if 'project_name' not in data:
            return Response({'error':'Please Provide project_name'},status=status.HTTP_406_NOT_ACCEPTABLE)
        if 'ProjectType' not in data:
            return Response({'error':'Please Provide ProjectType'},status=status.HTTP_406_NOT_ACCEPTABLE)
        if 'project_owner' not in data:
            return Response({'error':'Please Provide project_owner'},status=status.HTTP_406_NOT_ACCEPTABLE)

        try:
            projecttype = ProjectType.objects.get(id=data['ProjectType'])

        except(ObjectDoesNotExist):
            return Response({'error':'This Project Type Not Found'},status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({'error':'Please Cheak Your Datatype of project_type it must to need interger type convertable'},status=status.HTTP_400_BAD_REQUEST)
        
        try:
            projectowner = Client.objects.get(id=data['project_owner'])

        except(ObjectDoesNotExist):
            return Response({'error':'This Client Not Found'},status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({'error':'Please Cheak Your Datatype of project_owner it must to need interger type convertable'},status=status.HTTP_400_BAD_REQUEST)

        
        project = Project.objects.create(project_name = data['project_name'],ProjectType = projecttype,project_owner=projectowner,created_by = request.user)
        

        if 'starting_date' in data:
            project.starting_date = data['starting_date']
        
        if 'deadline' in data:

            project.deadline = data['deadline']

        if 'project_detatils' in data:
            project.project_detatils = data['project_detatils']

        if 'project_status' in data:
            project.project_status = data['project_status']

        if 'developer' in data:
            for i in data['developer']:

                try:
                    objj = Employee.objects.get(id=i)
                except(ObjectDoesNotExist):
                    return Response({'error':f'{i} id Employee Not Found'},status=status.HTTP_404_NOT_FOUND)
                
                # except:
                #     return Response({'error':'Please Cheak Your Datatype of Developer Array all item must need to integer or it must to need interger type convertable'},status=status.HTTP_400_BAD_REQUEST)

                project.developer.add(objj)


        project.save()

        return self.get(request)
    
class EditProjectAPIview(APIView):


    def get(self,request,pk):

        try:

            project = Project.objects.get(id=pk)
        except(ObjectDoesNotExist):

            return Response({'error':'Project Not Found In databas'},status=status.HTTP_404_NOT_FOUND)
        
        except:
            return Response({'error': 'please Cheak Your Datatype of your url primary key'},status=status.HTTP_400_BAD_REQUEST)
        
        ser = ProjectSerializer(project,context = {'request':request})

        return Response(ser.data,status=status.HTTP_200_OK)
    

    def put(self,request,pk):

        try:

            project = Project.objects.get(id=pk)
        except(ObjectDoesNotExist):

            return Response({'error':'Project Not Found In databas'},status=status.HTTP_404_NOT_FOUND)
        
        except:
            return Response({'error': 'please Cheak Your Datatype of your url primary key'},status=status.HTTP_400_BAD_REQUEST)
        
    
        data = request.data 

        if 'project_name' in data:

            project.project_name = data['project_name']

        if 'ProjectType' in data:

            project.ProjectType = data['ProjectType']

        if 'project_owner' in data:

            try:
                projectowner = Client.objects.get(id=data['project_owner'])

            except(ObjectDoesNotExist):
                return Response({'error':'This Client Not Found'},status=status.HTTP_404_NOT_FOUND)
            except:
                return Response({'error':'Please Cheak Your Datatype of project_owner it must to need interger type convertable'},status=status.HTTP_400_BAD_REQUEST)
            
            project.project_owner = projectowner

        if 'starting_date' in data:
            project.starting_date = data['starting_date']
        
        if 'deadline' in data:

            project.deadline = data['deadline']

        if 'project_detatils' in data:
            project.project_detatils = data['project_detatils']

        if 'project_status' in data:
            project.project_status = data['project_status']

        if 'developer' in data:

            for i in data['developer']:

                try:
                    objj = Employee.objects.get(id=i)
                except(ObjectDoesNotExist):
                    return Response({'error':f'{i} id Employee Not Found'},status=status.HTTP_404_NOT_FOUND)
                
                except:
                    return Response({'error':'Please Cheak Your Datatype of Developer Array all item must need to integer or it must to need interger type convertable'},status=status.HTTP_400_BAD_REQUEST)

                project.developer.add(objj)

        project.save()


        return self.get(self=self,request=request,pk=pk)
    


    def delete(self,request,pk):
        try:
            project = Project.objects.get(id=pk)
        except(ObjectDoesNotExist):
            return Response({'error':'Project Not Found In databas'},status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({'error': 'please Cheak Your Datatype of your url primary key'},status=status.HTTP_400_BAD_REQUEST)
        
        project.delete()

        return ProjectAPIview.get(self=self,request=request)
    





# Multiple Developer Can add into project . Multiple Developer Also neet to be remove...
    
