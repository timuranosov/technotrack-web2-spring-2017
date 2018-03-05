from django.db.models import Q
from rest_framework import serializers, viewsets, permissions

from application.api import router
from application.permissions import ReadOnly
from core.api import UserSerializer
from core.models import User
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Event
        fields = ('author', 'created', 'title',)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticated, ReadOnly)

    def get_queryset(self):
        q = super(EventViewSet, self).get_queryset()
        if self.request.query_params.get('username', None):
            username = self.request.query_params.get('username')
            friends = User.objects.all().filter(friends__author__username=username)
            q = q.filter(Q(author__username=username) | Q(author__in=friends))
        return q


router.register('events', EventViewSet)
