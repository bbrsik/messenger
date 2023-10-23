from django.urls import path
from . import views

urlpatterns = [
    path("chat/<chat_id>/", views.render_chat, name='render_chat'),
    path("chats/", views.render_list, name='render_list'),

    path("api/login/", views.login_view, name='login'),
    path("api/create/", views.create_message, name='create_message'),
    path("api/chat/create/", views.create_chat, name='create_chat'),
    path("api/chat/show/<chat_id>/", views.show_chat, name='show_chat'),
    path("api/chat/list/", views.list_chats, name='list_chats'),
]
