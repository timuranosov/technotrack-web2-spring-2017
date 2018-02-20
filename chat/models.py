# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from core.models import Named, Authored, Dated, User


class Chat(Named, Authored, Dated):
    pass

    class Meta:
        verbose_name = u'Чат'
        verbose_name_plural = u'Чаты'


class UserChat(models.Model):
    user = models.ForeignKey(User, related_name='user', verbose_name=u'пользователь')
    chat = models.ForeignKey(Chat, related_name='chats', verbose_name=u'чаты')

    class Meta:
        verbose_name = u'Пользовательский чат'
        verbose_name_plural = u'Пользовательские чаты'


class Message(Authored, Dated):
    content = models.TextField(max_length=1024, verbose_name=u'сообщение')
    chat = models.ForeignKey(Chat, related_name='messages', verbose_name=u'сообщения')

    class Meta:
        verbose_name = u'Сообщение'
        verbose_name_plural = u'Сообщения'

