from rest_framework import serializers
from .models import NPC, Map, Conversations, NPCsInLevel, UserGameItem

class NPCSerializer(serializers.ModelSerializer):
    class Meta:
        model = NPC
        fields = "__all__"

class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = ["level_ID"]

class ConversationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversations
        fields = "__all__"

class NPCsInLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NPCsInLevel
        fields = ["level_ID", "npc_ID"]

class UserGameItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGameItem
        fields = ["item_ID", "item_name"]