from django.shortcuts import render
from django.utils import timezone
from django.core import serializers
from django.http import HttpResponse
import datetime

# Create your views here.
from .models import Notification

""" def validate_number_date(num):
    if num < 10:
        num = '0' + str(num) """

def api_notification(request):
    obj_list = serializers.serialize('json', Notification.objects.filter(
        send_date__range=(
            datetime.datetime.now() - datetime.timedelta(minutes=15),
            datetime.datetime.now()
        )
    ))

    return HttpResponse(obj_list, content_type="application/json")