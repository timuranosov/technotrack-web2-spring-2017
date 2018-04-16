from django.db.models import Q
from rest_framework import serializers, viewsets, permissions
from rest_framework.pagination import PageNumberPagination

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
    last_message = serializers.SerializerMethodField('get_message')

    class Meta:
        model = Chat
        fields = ['pk', 'title', 'author', 'created', 'last_message']
        depth = 1

    @staticmethod
    def get_message(obj):
        last_message = obj.messages.all().order_by('-created')[0]
        avatar = None

        if last_message.author.avatar:
            avatar = last_message.author.avatar.url

        return {
            'author': last_message.author.username,
            'avatar': avatar,
            'content': last_message.content,
        }


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


class MessagePagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 200


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = MessagePagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        q = self.queryset.filter(chat__chats__user=self.request.user)
        chat_id = self.request.query_params.get('chat')
        if chat_id:
            q = q.filter(chat_id=chat_id)
        return q


router.register('chats', ChatViewSet)
router.register('userchats', UserChatViewSet)
router.register('messages', MessageViewSet)
