from django.contrib import admin

# Register your models here.
from .models import Job, Material, Department
admin.site.register(Job)
admin.site.register(Material) 
admin.site.register(Department)
 