from django.urls import path
from .views import profile, edit_profile, view_messages, delete_message, order_detail

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('edit/', edit_profile, name='edit_profile'),
    path('messages/', view_messages, name='view_messages'),
    path('messages/delete/<int:message_id>/',
         delete_message, name='delete_message'),
    path('order/<int:order_id>/', order_detail, name='order_detail'),
]
