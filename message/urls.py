from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name='login'),
    path("list/", views.list_messages, name='list_messages'),
    path("create/", views.create_message, name='create_message'),
    path("chat/create/", views.create_chat, name='create_chat')
]
