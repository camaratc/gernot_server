from django.contrib import admin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

# Register your models here.
from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
    search_fields = ('title', 'message', 'author', 'tag','creation_date', 'send_date')
    list_filter = ('title', 'author', 'tag', ('creation_date', DateTimeRangeFilter), ('send_date', DateTimeRangeFilter))
    list_display = ('title', 'message', 'author', 'tag', 'creation_date', 'send_date')
    ordering = ['-creation_date']

admin.site.register(Notification, NotificationAdmin)