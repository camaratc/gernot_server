from django.shortcuts import render
from django.utils import timezone
from django.core import serializers
import datetime

# Create your views here.
from .models import Notification

""" def validate_number_date(num):
    if num < 10:
        num = '0' + str(num) """

def api_notification(request):
    """ today = datetime.datetime.today()

    serialized_obj = serializers.serialize('json', Notification.objects.filter(
        send_date__year=today.year,
        send_date__month=validate_number_date(today.month),
        send_date__day=validate_number_date(today.day),
    )) """

    serialized_obj = serializers.serialize('json', Notification.objects.filter(
        send_date__range=(
            datetime.datetime.now() - datetime.timedelta(minutes=15),
            datetime.datetime.now()
        )
    ))

    return render(request, 'notification.html', { 'json': serialized_obj })