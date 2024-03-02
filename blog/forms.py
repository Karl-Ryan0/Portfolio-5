from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """
    Form for creating and updating Post instances.
    This form is linked to the Post model and allows users
    to input data for the fields
    title, body, main_image, body_image, and recipe.
    Custom labels are provided for each
    field to enhance the form's readability and user experience.
    """
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
