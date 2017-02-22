from rest_framework import serializers

from django.contrib.auth import get_user_model

from users.models import PlayList
from songs.api.serializers import SongSerializer
from songs.models import Song

User = get_user_model()


class PlaylistSerializer(serializers.ModelSerializer):

	class Meta:
		model = PlayList
		fields = ['name', 'songs', ]

	def __init__(self, *args, **kwargs):
		request = kwargs['context']['request']
		if request.method == "GET":
			self.fields['songs'] = SongSerializer(
				read_only=True, many=True)
		super(PlaylistSerializer, self).__init__(*args, **kwargs)
