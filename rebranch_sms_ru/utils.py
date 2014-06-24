# -*- coding: utf8 -*-

class CeleryMessageMixin(object):
    QUEUE_TYPE_PERIODIC = 0
    QUEUE_TYPE_MOMENTARY = 1

    QUEUE_TYPE_CHOICES = (
        (QUEUE_TYPE_PERIODIC, u'Периодический'),
        (QUEUE_TYPE_MOMENTARY, u'Моментальный'),
    )

    def send_async(self):
        raise NotImplementedError