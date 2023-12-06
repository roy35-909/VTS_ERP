from django.db import models
from user.models import *





class Service(models.Model):
    name = models.CharField(max_length=500)
    photo = models.ImageField(upload_to='Service/',null=True,blank=True)
    details = models.TextField(max_length=1000)
    amount_of_service = models.IntegerField(default=0)


    def __str__(self) -> str:
        return self.name


class Review(models.Model):

    client = models.ForeignKey(Client,on_delete=models.PROTECT, null=True, blank=True)
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    review = models.TextField(max_length=1000)
    

    def __str__(self) -> str:
        return f'{self.client.user.email} Review ==> {self.review}'