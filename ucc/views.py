# Create your views here.

from drf_haystack.viewsets import HaystackViewSet

from application.api import router
from .models import Post
from .search_api import PostSearchSerializer


class PostSearchView(HaystackViewSet):
    index_models = [Post]

    serializer_class = PostSearchSerializer


router.register('posts/search', PostSearchView, base_name='posts-search')
