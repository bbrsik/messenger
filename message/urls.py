from django.urls import path, include
from . import views, api_views

urlpatterns = [
    path("chat/<chat_id>/", views.render_chat, name='render_chat'),
    path("chats/", views.render_list, name='render_list'),

    path('api/', include([
        path("login/", api_views.login_view, name='login'),
        path("message/create/<chat_id>/", api_views.create_message, name='create_message'),

        path('chat/', include([
            path("create/", api_views.create_chat, name='create_chat'),
            path("show/<chat_id>/", api_views.show_chat, name='show_chat'),
            path("list/", api_views.list_chats, name='list_chats'),
        ])),
    ])),
]
