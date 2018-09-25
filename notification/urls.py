from django.urls import path
from django.views.generic.base import RedirectView

from . import views

app_name = 'api'

urlpatterns = [
    path('', RedirectView.as_view(url='notification/', permanent=False), name='index'),
    path('notification/', views.api_notification, name='api_notification'),
]