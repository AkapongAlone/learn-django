from rest_framework import viewsets
from .models import Room,Player
from .serializers import RoomSerializer,PlayerSerializer

class RoomViewSet(viewsets.ModelViewSet):
	queryset = Room.objects.all()
	serializer_class = RoomSerializer