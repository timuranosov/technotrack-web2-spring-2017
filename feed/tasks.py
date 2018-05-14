import datetime

from celery import task
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from templated_email import send_templated_mail, get_templated_mail

from core.models import User
from .models import Event


@task(bind=True, default_retry_delay=10)
def event_creator(self, instance_id, type_id):
    type = ContentType.objects.get_for_id(type_id)
    instance = type.get_object_for_this_type(id=instance_id)
    Event.objects.create(content_object=instance, author=instance.get_author(), title=instance.get_description())


@task(bind=True)
def send_to_subscribers(self, id):
    from django.db.models import Q
    yesterday = timezone.now() - datetime.timedelta(15)
    query = Event.objects.all() \
        .filter(Q(author__friendship__friend__id=id) & Q(created__gt=yesterday)) \
        .distinct().order_by('-created').prefetch_related('author', 'content_object')

    user = User.objects.get(pk=id)
    recipient_list = [user.email, ]
    if settings.DEBUG:
        recipient_list = [admin[0] for admin in settings.ADMINS]

    event_list = list(query)
    context = {
        'events': event_list,
        'user': user,
    }

    email = get_templated_mail('subscribe', context, 'soNet@sub.ru', recipient_list)
    email.send()

    return user.email


@task(bind=True)
def send_results_to_admins(self, emails):
    recipient_list = [admin[0] for admin in settings.ADMINS]
    send_templated_mail('subscribe_result', 'soNet@sub.ru', recipient_list, {
        'emails': emails,
    })
