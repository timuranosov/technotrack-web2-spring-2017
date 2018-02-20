from __future__ import unicode_literals

from django.apps import AppConfig


class FriendsConfig(AppConfig):
    name = 'friends'

    def ready(self):
        import friends.signals
