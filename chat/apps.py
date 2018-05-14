from __future__ import unicode_literals

from django.apps import AppConfig


class ChatConfig(AppConfig):
    name = 'chat'

    def ready(self):
        import chat.signals
        import chat.api
        import chat.search_api
