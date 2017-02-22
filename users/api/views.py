from django.contrib.auth import get_user_model

from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView, 
    ListCreateAPIView
)

from rest_framework.permissions import IsAuthenticated

from users.models import PlayList
from .serializers import PlaylistSerializer

User = get_user_model()


class PlaylistCreateListAPIView(ListCreateAPIView):
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return PlayList.objects.filter(fk_user=user)

    def perform_create(self,serializer):
        serializer.save(fk_user=self.request.user)
        

class PlaylistDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class =  PlaylistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PlayList.objects.filter(
            fk_user=self.request.user)

