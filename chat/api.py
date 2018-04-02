from django.db.models import Q
from rest_framework import serializers, viewsets, permissions

from application.api import router
from application.permissions import IsOwnerOrReadOnly
from core.api import UserSerializer
from .models import Chat, UserChat, Message


class MessageSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default='author.id')

    def validate(self, data):
        if UserChat.objects.filter(Q(user=self.context['request'].user) & Q(chat=data['chat'])).exists():
            return data
        else:
            raise serializers.ValidationError("Not in chat")

    class Meta:
        model = Message
        fields = ['content', 'author', 'created', 'chat']


class ChatSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    messages = MessageSerializer(many=True)

    class Meta:
        model = Chat
        fields = ['pk', 'title', 'author', 'created', 'messages', ]
        depth = 1


class UserChatSerializer(serializers.HyperlinkedModelSerializer):
    chat = ChatSerializer()

    class Meta:
        model = UserChat
        fields = ['chat', ]
        depth = 1


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        q = super(ChatViewSet, self).get_queryset()
        if self.request.query_params.get('username'):
            username = self.request.query_params.get('username')
            q = q.filter(chats__user__username=username)
        return q


class UserChatViewSet(viewsets.ModelViewSet):
    queryset = UserChat.objects.all()
    serializer_class = UserChatSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        q = super(UserChatViewSet, self).get_queryset()
        if self.request.query_params.get('username'):
            q = q.filter(user__username=self.request.query_params.get('username'))
        return q


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        chat_id = self.request.query_params.get('chat')
        if chat_id:
            query = Q(chat__chats__user=self.request.user) & Q(chat__id=chat_id)
        else:
            query = Q(chat__chats__user=self.request.user)
        return self.queryset.filter(query)


router.register('chats', ChatViewSet)
router.register('userchats', UserChatViewSet)
router.register('messages', MessageViewSet)
