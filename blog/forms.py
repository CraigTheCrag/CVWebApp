from django import forms
from .models import Post, Project

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'text', 'video_id')