import django.db.models.signals as signals
from django.dispatch import receiver
from .models import FriendRequest, Friendship


@receiver(signals.post_init, sender=FriendRequest)
def pre_save_approve_create_friendship(instance, *args, **kwargs):
    instance.approved_was = instance.approved


@receiver(signals.post_save, sender=FriendRequest)
def post_save_approve_create_friendship(instance, created=False, *args, **kwargs):
    if not instance.approved_was and instance.approved:
        Friendship.objects.create(first=instance.initiator, second=instance.recipient)
        Friendship.objects.create(first=instance.recipient, second=instance.initiator)


@receiver(signals.post_delete, sender=FriendRequest)
def post_delete_friend(instance, *args, **kwargs):
        Friendship.objects.get(first=instance.initiator, second=instance.recipient).delete()
        Friendship.objects.get(first=instance.recipient, second=instance.initiator).delete()
