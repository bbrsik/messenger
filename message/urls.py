from django.urls import path, include
from . import views, api_views

urlpatterns = [
    path("chat/<chat_id>/", views.render_chat, name='render_chat'),
    path("chats/", views.render_list, name='render_list'),
    path("login/", views.render_login, name='render_login'),
    path("signup/", views.render_signup, name='render_signup'),

    path('api/', include([
        path("logout/", api_views.logout_view, name='logout_view'),
        path("create_user/", api_views.create_user, name='create_user'),

        path('message/', include([
            path("create/<chat_id>/", api_views.create_message, name='create_message'),
            path("delete/<message_id>/", api_views.delete_message, name='delete_message'),
        ])),

        path('chat/', include([
            path("create/", api_views.create_chat, name='create_chat'),
        ])),
    ])),
]
