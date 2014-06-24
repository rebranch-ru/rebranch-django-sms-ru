# -*- coding:utf-8 -*-
import re
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from rebranch_django_sms_ru.utils import CeleryMessageMixin
from rebranch_sms_ru.statuses import STATUS_CHOICES
# from rebranch_sms_ru.utils import clean_phone


class Message(models.Model, CeleryMessageMixin):
    # Content-object field
    content_type = models.ForeignKey(ContentType,
                                     null=True,
                                     blank=True,
                                     verbose_name=u'content type',
                                     related_name=u'content_type_set_for_%(class)s')
    object_id = models.CharField(u'object ID', max_length=10, null=True, blank=True)
    content_object = generic.GenericForeignKey(ct_field=u'content_type', fk_field=u'object_id')
    #

    recipient = models.CharField(u'Получатель', max_length=11)
    content = models.TextField(u'Сообщение')
    api_id = models.CharField(u'ID в системе рассылки', max_length=255, null=True, blank=True)
    sent = models.DateTimeField(u'Дата отправки', null=True, blank=True)
    queue_type = models.IntegerField(u'Тип очереди', choices=CeleryMessageMixin.QUEUE_TYPE_CHOICES)
    status = models.IntegerField(u'Статус', choices=STATUS_CHOICES.items(), null=True, blank=True)
    cost = models.DecimalField(u'Стоимость', null=True, blank=True, decimal_places=3, max_digits=10)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = u'SMS-сообщение'
        verbose_name_plural = u'SMS-сообщения'
        ordering = [u'-created']
        db_table = u'sms_ru_message'

    def __unicode__(self):
        return self.recipient

    # clean_phone = staticmethod(clean_phone)

    def send_async(self):
        from rebranch_django_sms_ru.tasks import send_message_momentary

        send_message_momentary.apply_async(kwargs={u'message_id': self.id})


from .tasks import *