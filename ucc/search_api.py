from .api import PostSerializer
from .search_indexes import PostIndex


class PostSearchSerializer:

    @staticmethod
    def to_representation(instance):
        return PostSerializer(instance.object).to_representation(instance.object)

    class Meta:
        # The `index_classes` attribute is a list of which search indexes
        # we want to include in the search.
        index_classes = [PostIndex]

        # The `fields` contains all the fields we want to include.
        # NOTE: Make sure you don't confuse these with model attributes. These
        # fields belong to the search index!
        fields = [
            "text", "title"
        ]
