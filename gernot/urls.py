from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', RedirectView.as_view(url='admin/', permanent=False), name='index'),
    path('admin/', admin.site.urls),
]
