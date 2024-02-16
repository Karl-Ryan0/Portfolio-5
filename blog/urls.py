from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('create/', views.create_article, name='create_article'),
]
