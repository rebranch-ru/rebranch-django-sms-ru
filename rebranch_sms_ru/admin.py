#encoding=utf8
from django.contrib import admin
from django.conf import settings

from rebranch_sms_ru.models import Message
from rebranch_sms_ru.statuses import STATUS_CHOICES


class RawStatusSimpleListFilter(admin.SimpleListFilter):
    title = u'Код статуса'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        lookups_choices = tuple([(status, status) for status in STATUS_CHOICES.keys()])
        return lookups_choices

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(status=self.value())
        else:
            return queryset


class MessageModelAdmin(admin.ModelAdmin):
    list_display = (u'recipient', u'api_id', u'sent', u'queue_type', u'status_raw', u'status')
    if getattr(settings, u'SMS_RU_STORE_SMS_COST', False):
        list_display += (u'cost',)

    def status_raw(self, obj):
        return obj.status

    search_fields = (u'recipient', u'api_id')
    list_filter = (u'queue_type', RawStatusSimpleListFilter)

    status_raw.allow_tags = True
    status_raw.short_description = u'Код статуса'


admin.site.register(Message, MessageModelAdmin)