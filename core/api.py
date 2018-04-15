from django.db.models import Q
from rest_framework import serializers, viewsets, permissions, fields

from application.api import router
from application.permissions import IsOwnerOrReadOnly
from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    username = fields.ReadOnlyField()

    class Meta:
        model = User
        fields = ('pk', 'username', 'first_name', 'last_name', 'avatar')
        depth = 3


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def get_queryset(self):
        q = self.queryset
        if 'pk' in self.kwargs:
            pk = self.kwargs['pk']
            return q.filter(
                (Q(friendship__friend=self.request.user) | Q(pk=self.request.user.pk)) & Q(pk=pk)).distinct()

        username = q.query_params.get('username')
        if username:
            return q.filter(username=username)
        return q.filter(pk=self.request.user.pk)


router.register('users', UserViewSet)
