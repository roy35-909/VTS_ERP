from django.contrib import admin
from .models import User,Employee,Admin,Client

admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Admin)
admin.site.register(Client)
# Register your models here.
