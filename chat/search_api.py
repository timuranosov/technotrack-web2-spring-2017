from .api import MessageSerializer
from .search_indexes import MessageIndex


class MessageSearchSerializer:

    @staticmethod
    def to_representation(instance):
        return MessageSerializer(instance.object).to_representation(instance.object)

    class Meta:
        # The `index_classes` attribute is a list of which search indexes
        # we want to include in the search.
        index_classes = [MessageIndex]

        # The `fields` contains all the fields we want to include.
        # NOTE: Make sure you don't confuse these with model attributes. These
        # fields belong to the search index!
        fields = [
            "text", "title"
        ]
