from django.db import models
from user.models import *
class ProjectType(models.Model):
    name = models.CharField(max_length=500)
    thumbline = models.CharField(max_length=500)
    created_by = models.ForeignKey(User,on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name
    


class Project(models.Model):

    PROJECT_STATUS = [
        ("PENDING", "Pending"),
        ("UI/UX_WORKING", "UI/UX_Working"),
        ("IN_DEVELOPMENT", "IN_Development"),
        ("IN_TESTING", "IN_Testing"),
        ("IN_DEPLOYMENT", "IN_Deployment"),
        ("COMPLETE", "Complete"),
    ]

    project_name = models.CharField(max_length=500)
    ProjectType = models.ForeignKey(ProjectType,on_delete=models.PROTECT)
    starting_date = models.DateField(null=True,blank=True)
    deadline = models.DateField(null=True, blank=True)
    developer = models.ManyToManyField(Employee,null=True,blank=True)
    project_owner = models.ForeignKey(Client,on_delete=models.PROTECT)
    project_detatils = models.TextField(max_length=1000,null=True,blank=True)
    created_by = models.ForeignKey(User,on_delete=models.PROTECT)
    project_status = models.CharField(max_length=80, choices=PROJECT_STATUS, blank=False, null=False,
                            default="PENDING")


    def __str__(self) -> str:
        return f"{self.project_name} ==> Client : {self.project_owner.user.first_name} {self.project_owner.user.last_name}"
    



