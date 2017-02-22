from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView,ListAPIView
from rest_framework.permissions import IsAuthenticated

from songs.models import Song
from .serializers import SongSerializer
from .permissions import UserPermissions


class SongDetialAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated,UserPermissions]


class SongCreateAPIView(ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated,UserPermissions]



