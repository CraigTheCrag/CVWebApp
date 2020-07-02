from django.contrib import admin
from .models import Post, Project

myModels = [Post, Project]

admin.site.register(myModels)