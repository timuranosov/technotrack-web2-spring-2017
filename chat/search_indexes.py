import datetime
from haystack import indexes
from .models import Message


class MessageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title', use_template=True)
    author = indexes.CharField(model_attr='author')
    created = indexes.DateTimeField(model_attr='created')

    def get_model(self):
        return Message

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(created__lte=datetime.datetime.now())