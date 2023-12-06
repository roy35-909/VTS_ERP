from django.db import models
from user.models import User

class Meeting(models.Model):
    meet_title = models.CharField(max_length=255)
    meet_link = models.URLField()
    meet_docs = models.FileField(upload_to='Meeting_Docs/',null=True,blank=True)
    meet_detatils = models.TextField(max_length=1000, null=True, blank=True)
    meet_attender = models.ManyToManyField(User)
    meet_time = models.DateTimeField()



    def __str__(self) -> str:
        return f'{self.meet_title} ===> at {self.meet_time}'
    

    