from rest_framework import serializers
from .models import NPC

class NPCSerializer(serializers.ModelSerializer):
    class Meta:
        model = NPC
        fields = ["id", "name", "img"]