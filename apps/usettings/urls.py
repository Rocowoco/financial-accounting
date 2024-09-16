from django.urls import path
from . import views

urlpatterns = [
    path('', views.SettingsView.as_view(), name='settings'),
]
