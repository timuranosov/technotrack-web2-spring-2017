from rest_framework import serializers, viewsets, permissions, fields

from application.api import router
from application.permissions import IsOwnerOrReadOnly
from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    username = fields.ReadOnlyField()
    first_name = fields.SerializerMethodField('get_first_name_to_friend')
    last_name = fields.SerializerMethodField('get_last_name_to_friend')
    isFriend = fields.SerializerMethodField('check_friend')

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'avatar', 'isFriend')
        depth = 3

    def get_first_name_to_friend(self, obj):
        request = self.context['request']

        if obj.friends.filter(friend__id=request.user.id).exists() or request.user.is_staff or obj == request.user:
            return obj.first_name
        return None

    def get_last_name_to_friend(self, obj):
        request = self.context['request']
        if obj.friends.filter(friend__id=request.user.id).exists() or request.user.is_staff or obj == request.user:
            return obj.last_name
        return None

    def check_friend(self, obj):
        return obj.friends.all().filter(author=self.context['request'].user).exists()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def get_queryset(self):
        q = self.queryset
        username = self.request.query_params.get('username')
        if 'pk' in self.kwargs:
            pk = self.kwargs['pk']
            q = q.filter(pk=pk)
        elif username:
            q = q.filter(username=username)
        else:
            q = q.filter(pk=self.request.user.pk)
        return q


router.register('users', UserViewSet)
