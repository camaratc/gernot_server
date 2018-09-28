from django.shortcuts import render
from django.utils import timezone
from django.core import serializers
from django.http import HttpResponse
from django.db.models import F, Func
import datetime

from .models import Notification

def api_notification(request):
    lasts_forever = Notification.objects.filter(time_active__lte=0)

    temp_notification = Notification.objects.annotate(
        duration=F('time_active'),
    ).filter(
        time_active__gt=0,
        send_date__range=(
            # datetime.datetime.now() - datetime.timedelta(minutes=F('time_active')),
            datetime.datetime.now() - datetime.timedelta(minutes=15),
            datetime.datetime.now()
        )
    )

    print(lasts_forever)
    print(temp_notification)

    obj_list = []

    for j in temp_notification:
        obj_list.append(j)
    for i in lasts_forever:
        obj_list.append(i)

    obj_list = serializers.serialize('json', obj_list)

    """ obj_list = serializers.serialize('json', Notification.objects.filter(
        send_date__range=(
            datetime.datetime.now() - datetime.timedelta(minutes=15),
            datetime.datetime.now()
        )
    )) """

    return HttpResponse(obj_list, content_type="application/json")

def info_notification(request):
    notification = serializers.serialize('json', Notification.objects.all())

    return HttpResponse(notification, content_type="application/json")