from django.db.models import Q
from django.utils import timezone
from rest_framework import serializers, viewsets, permissions

from application.api import router
from application.permissions import IsOwnerOrReadOnly
from .models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)
    created = serializers.DateTimeField(read_only=True, format='%X %d %b %Y')

    class Meta:
        model = Post
        fields = ('pk', 'content', 'author', 'created', 'likes_count')


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, created=timezone.now())

    def get_queryset(self):
        q = self.queryset
        if 'pk' in self.kwargs:
            pk = self.kwargs['pk']
            return q.filter((Q(author__friendship__friend=self.request.user) | Q(author=self.request.user)) & Q(pk=pk))\
                .distinct()
        username = self.request.query_params.get('username')
        if username != self.request.user.username and username is not None:
            q = q.filter(Q(author__friendship__friend=self.request.user) & Q(author__username=username))
        else:
            q = q.filter(author=self.request.user)
        return q


router.register('posts', PostViewSet)
