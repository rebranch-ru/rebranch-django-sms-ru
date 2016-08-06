# -*- coding:utf-8 -*-
from django.contrib import admin
from functools import partial


class CeleryMessageMixin(object):
    QUEUE_TYPE_PERIODIC = 0
    QUEUE_TYPE_MOMENTARY = 1

    QUEUE_TYPE_CHOICES = (
        (QUEUE_TYPE_PERIODIC, u'Периодический'),
        (QUEUE_TYPE_MOMENTARY, u'Моментальный'),
    )

    def send_async(self):
        raise NotImplementedError


class ModelAdminWithFKLink(admin.ModelAdmin):
    """
    ModelAdmin позволяющий отображать связанные объекты модели со ссылками:
    пример:
    def link_to_deal(self, instance):
        return self.__getattr__('link_to_shipping__deal')(instance)

    link_to_deal.allow_tags = True
    """

    def __getattr__(self, name, *args, **kwargs):
        def foreign_key_link(instance, field_raw):
            fields = field_raw.split(u'__')
            target = instance
            for field in fields:
                target = getattr(target, field)
            if target:
                return u'<a href="../../%s/%s/%d/">%s</a>' % (
                    target._meta.app_label, target._meta.module_name, target.id, unicode(target)
                )
            else:
                return None

        if name[:8] == 'link_to_':
            method = partial(foreign_key_link, field_raw=name[8:])
            method.__name__ = name[8:]
            method.allow_tags = True
            setattr(self, name, method)
            return getattr(self, name)
        raise AttributeError
