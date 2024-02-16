from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'main_image', 'body_image', 'recipe']
        labels = {
            'title': 'Article Title',
            'body': 'Article Content',
            'main_image': 'Top Image',
            'body_image': 'Body Image',
            'recipe': 'Article Recipe',
        }
