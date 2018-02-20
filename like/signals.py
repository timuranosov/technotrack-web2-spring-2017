# coding: utf-8

import django.db.models.signals as signals
from .models import Like, LikeAble

likes_for_achieve = 2


def post_init_like(instance, *args, **kwargs):
    if instance.content_object:
        instance.likes_was = instance.content_object.likes.count()


def create_like(instance, *args, **kwargs):
    if instance.content_object.likes.count() == likes_for_achieve:
        instance.objects.create(content_object=instance.content_object, title=u'100 лайков')


def delete_like(instance, *args, **kwargs):
    if instance.likes_was == likes_for_achieve:
        instance.content_object.achieve.first().delete()


signals.post_init.connect(post_init_like, sender=Like)
signals.post_save.connect(create_like, sender=Like)
signals.pre_delete.connect(delete_like, sender=Like)
