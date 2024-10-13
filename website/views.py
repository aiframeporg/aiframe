from django.shortcuts import render, get_object_or_404
from .models import Blog, ModelPost, Tutorial
from .models import DownloadableApp

def home(request):
    app = DownloadableApp.objects.first()  # Replace with specific logic if needed
    return render(request, 'website/index.html', {'app': app})

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'website/blog_list.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'website/blog_detail.html', {'blog': blog})

def model_list(request):
    models = ModelPost.objects.all()
    return render(request, 'website/model_list.html', {'models': models})

def model_detail(request, model_id):
    model = get_object_or_404(ModelPost, id=model_id)
    return render(request, 'website/model_detail.html', {'model': model})

def tutorial_list(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'website/tutorial_list.html', {'tutorials': tutorials})

def tutorial_detail(request, tutorial_id):
    tutorial = get_object_or_404(Tutorial, id=tutorial_id)
    return render(request, 'website/tutorial_detail.html', {'tutorial': tutorial})

def download_page(request):
    # Get the latest downloadable application
    app = DownloadableApp.objects.order_by('-created_at').first()
    return render(request, 'website/download.html', {'app': app})