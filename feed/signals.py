import django.db.models.signals as signals
from .models import EventAble, Event


def create_event(instance, *args, **kwargs):
    print(instance.get_author().pk)
    if not instance.event.exists():
        Event.objects.create(content_object=instance, author=instance.get_author(), title=instance.get_description())


def delete_event(instance, *args, **kwargs):
    instance.event.remove()


for model in EventAble.__subclasses__():
    signals.post_save.connect(create_event, sender=model)
    signals.pre_delete.connect(delete_event, sender=model)
