from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Post, Project
from .forms import PostForm, ProjectForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts' : posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if (request.method == "POST"):
        form = PostForm(request.POST)
        if (form.is_valid):
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if (request.method == "POST"):
        form = PostForm(request.POST, instance=post)
        if (form.is_valid):
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')

    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def project_list(request):
    projects = Project.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/project_list.html', {'projects' : projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'blog/project_detail.html', {'project': project})

@login_required
def project_new(request):
    if (request.method == "POST"):
        form = ProjectForm(request.POST)
        if (form.is_valid):
            project = form.save(commit=False)
            project.author = request.user
            project.video_id = form.cleaned_data["video_id"]
            project.github_title = form.cleaned_data["github_title"]
            project.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'blog/project_edit.html', {'form': form})

@login_required
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if (request.method == "POST"):
        form = ProjectForm(request.POST, instance=project)
        if (form.is_valid):
            project = form.save(commit=False)
            project.author = request.user
            project.video_id = form.cleaned_data["video_id"]
            project.github_title = form.cleaned_data["github_title"]
            project.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'blog/project_edit.html', {'form': form})

@login_required
def project_draft_list(request):
    projects = Project.objects.filter(published_date__isnull=True).order_by('created_date')

    return render(request, 'blog/project_draft_list.html', {'projects': projects})

@login_required
def project_publish(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.publish()
    return redirect('project_detail', pk=pk)

@login_required
def project_remove(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return redirect('project_list')