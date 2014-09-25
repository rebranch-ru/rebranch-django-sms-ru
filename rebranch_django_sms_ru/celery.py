from __future__ import absolute_import
from django.conf import settings

from celery import Celery

app = Celery(backend=settings.CELERY_RESULT_BACKEND, broker=settings.BROKER_URL)