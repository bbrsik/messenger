from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('message/', include('message.urls')),
    path('user/', include('user.urls')),
    path('', views.redirect_view, name='redirect_view'),
]
