from haystack import indexes
from songs.models import Song


class SongIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    song_title = indexes.CharField(model_attr='song_title')
    artist = indexes.CharField(model_attr='artist')

    def get_model(self):
        return Song

    def index_queryset(self, using=None):
        return self.get_model().objects.all()