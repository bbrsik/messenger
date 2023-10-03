from django.urls import path
from . import views

urlpatterns = [
    path("chat/<chat_id>/", views.render_chat, name='render_chat'),
    path("chat/list/", views.list_chats, name='list_chats'),
    # api todo вынести в /api/...
    path("login/", views.login_view, name='login'),
    path("create/", views.create_message, name='create_message'),
    path("chat/create/", views.create_chat, name='create_chat'),
    path("chat/show/<chat_id>/", views.show_chat, name='show_chat'),
    path("api/chat/list/", views.list_chats, name='list_chats'),
]
