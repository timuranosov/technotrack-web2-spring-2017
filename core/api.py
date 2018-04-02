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
        username = self.request.query_params.get('username')
        if username:
            return self.queryset.filter(username=username)
        return self.queryset.filter(pk=self.request.user.pk)


router.register('users', UserViewSet)
