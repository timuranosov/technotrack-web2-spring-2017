# Create your views here.

from drf_haystack.viewsets import HaystackViewSet

from application.api import router
from .models import Message
from .search_api import MessageSearchSerializer


class PostSearchView(HaystackViewSet):
    index_models = [Message]

    serializer_class = MessageSearchSerializer


router.register('messages/search', PostSearchView, base_name='messages-search')
