from django.db.models import Q
from generic_relations.relations import GenericRelatedField
from rest_framework import serializers, viewsets, permissions

from application.api import router
from application.permissions import ReadOnly
from friends.models import Friendship
from ucc.models import Post
from .models import Event, Achieve


class EventSerializer(serializers.HyperlinkedModelSerializer):
    content_object = GenericRelatedField({
        Achieve: serializers.HyperlinkedRelatedField(view_name='achieve-detail', read_only=True),
        Friendship: serializers.HyperlinkedRelatedField(view_name='friendship-detail', read_only=True),
        Post: serializers.HyperlinkedRelatedField(read_only=True, view_name='post-detail'),
    })

    class Meta:
        model = Event
        fields = ('author', 'created', 'title', 'content_object', 'id')
        depth = 0


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticated, ReadOnly)

    def get_queryset(self):
        q = self.queryset
        q = q.filter(Q(author=self.request.user) | Q(author__friendship__friend=self.request.user)).distinct()
        return q


class AchieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achieve
        fields = ('title',)


class AchieveViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Achieve.objects.all()
    serializer_class = AchieveSerializer
    permission_classes = (permissions.IsAuthenticated, ReadOnly)

    def get_queryset(self):
        return Achieve.objects.none()


class UserEventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticated, ReadOnly)

    def get_queryset(self):
        q = self.queryset
        username = self.request.query_params.get('username')
        if username and username != self.request.user.username:
            q = q.filter(Q(author__username=username) & Q(author__friendship__friend=self.request.user))
            return q
        return q.filter(author=self.request.user)


router.register('events', EventViewSet)
router.register('achieve', AchieveViewSet)
