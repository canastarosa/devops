from rest_framework import serializers
from .models import Image


class UpdateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'file',)
