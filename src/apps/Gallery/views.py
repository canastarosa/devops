from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UpdateImageSerializer
from .models import Image


class UpdateImageView(ListCreateAPIView):
    serializer_class = UpdateImageSerializer

    def get_queryset(self):
        return Image.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DetailImageView(RetrieveUpdateDestroyAPIView):
    serializer_class = UpdateImageSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Image.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)