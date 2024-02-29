from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

# Create your models here.

User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    blog_mailing_list = models.BooleanField(default=False)
    shopping_mailing_list = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.profile.save()


class BlogSubscriber(get_user_model()):
    class Meta:
        proxy = True
        verbose_name = 'Blog Subscriber'
        verbose_name_plural = 'Blog Subscribers'


class ShopSubscriber(get_user_model()):
    class Meta:
        proxy = True
        verbose_name = 'Shop Subscriber'
        verbose_name_plural = 'Shop Subscribers'
