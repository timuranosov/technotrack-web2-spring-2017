from __future__ import unicode_literals

from django.apps import AppConfig


class UccConfig(AppConfig):
    name = 'ucc'

    def ready(self):
        import ucc.signals