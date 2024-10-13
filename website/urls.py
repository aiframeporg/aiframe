from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage
    path('blogs/', views.blog_list, name='blog_list'),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('models/', views.model_list, name='model_list'),
    path('model/<int:model_id>/', views.model_detail, name='model_detail'),
    path('tutorials/', views.tutorial_list, name='tutorial_list'),
    path('tutorial/<int:tutorial_id>/', views.tutorial_detail, name='tutorial_detail'),
    path('download/', views.download_page, name='download_page'),
]
