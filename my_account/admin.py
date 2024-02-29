from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UserProfile, BlogSubscriber, ShopSubscriber


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profile'
    fk_name = 'user'


class CustomUserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


class BlogSubscriberAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(profile__blog_mailing_list=True)


class ShopSubscriberAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(profile__shopping_mailing_list=True)


admin.site.register(BlogSubscriber, BlogSubscriberAdmin)
admin.site.register(ShopSubscriber, ShopSubscriberAdmin)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
