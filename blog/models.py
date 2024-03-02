from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Post(models.Model):
    """
    A model representing a blog post.
    The posts are ordered by their creation date,
    with the most recently created posts appearing first.
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    main_image = CloudinaryField('image')
    body_image = CloudinaryField('image')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    recipe = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_on']
