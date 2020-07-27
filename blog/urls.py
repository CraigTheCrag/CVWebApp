from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('posts/', views.post_list, name="post_list"),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('projects/', views.project_list, name='project_list'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('project/new/', views.project_new, name='project_new'),
    path('project/<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('project/drafts/', views.project_draft_list, name='project_draft_list'),
    path('project/<pk>/publish/', views.project_publish, name='project_publish'),
    path('project/<pk>/remove/', views.project_remove, name='project_remove'),
]