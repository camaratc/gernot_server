from django.shortcuts import render
from django.utils import timezone
from django.core import serializers

# Create your views here.
from .models import Notification

def api_notification(request):
    serialized_obj = serializers.serialize('json', Notification.objects.all())

    return render(request, 'notification.html', { 'json': serialized_obj })