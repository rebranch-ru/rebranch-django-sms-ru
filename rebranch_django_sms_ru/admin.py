#encoding=utf8
from django.contrib import admin
from django.conf import settings

from rebranch_django_sms_ru.utils import ModelAdminWithFKLink
from rebranch_django_sms_ru.models import Message
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


class MessageModelAdmin(ModelAdminWithFKLink):
    search_fields = (u'recipient', u'api_id')
    list_filter = (u'queue_type', RawStatusSimpleListFilter)

    list_display = (
    u'recipient', u'api_id', u'sent', u'queue_type', u'status_raw', u'status', u'link_to_content_object')
    if getattr(settings, u'SMS_RU_STORE_SMS_COST', False):
        list_display += (u'cost',)

    def status_raw(self, obj):
        return obj.status

    status_raw.allow_tags = True
    status_raw.short_description = u'Код статуса'

    def link_to_content_object(self, instance):
        return self.__getattr__('link_to_content_object')(instance)

    link_to_content_object.allow_tags = True
    link_to_content_object.short_description = u'Связанный объект'


admin.site.register(Message, MessageModelAdmin)