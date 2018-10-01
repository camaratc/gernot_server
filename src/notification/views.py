from django.shortcuts import render
from django.utils import timezone
from django.core import serializers
from django.http import HttpResponse
import datetime

from .models import Notification
  
def api_notification(request):
    obj_list = []

    lasts_forever = Notification.objects.filter(time_active__lte=0)
    temp_notification = []

    sql = 'SELECT * FROM notification_notification WHERE time_active != 0'

    for item in Notification.objects.raw(sql):
        obj = Notification.objects.filter(
            pk = item.id,
            send_date__range=(
                datetime.datetime.now() - datetime.timedelta(minutes=item.time_active),
                datetime.datetime.now()
            )
        ).first()

        if obj != None:
            temp_notification.append(obj)

    for j in temp_notification:
        obj_list.append(j)
    for i in lasts_forever:
        obj_list.append(i)

    # Ordenar a lista pelo tempo ativo

    obj_list.sort(key=lambda x: x.time_active, reverse=False)

    # Mandar as notificações permanentes para o final da lista
    count = 0
    for a in range(len(obj_list)):
        while obj_list[a].time_active == 0:
            if count == len(obj_list):
                break
            obj_list += [obj_list.pop(a)]
            count += 1

    obj_list = serializers.serialize('json', obj_list)
    return HttpResponse(obj_list, content_type="application/json")

def info_notification(request):
    notification = serializers.serialize('json', Notification.objects.all())

    return HttpResponse(notification, content_type="application/json")