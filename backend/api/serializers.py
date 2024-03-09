from rest_framework import serializers
from .models import NPC, Map, UserDialouge, NPCDialouge, NPCsInLevel, UserGameItem

class NPCSerializer(serializers.ModelSerializer):
    class Meta:
        model = NPC
        fields = ["npc_ID", "name"]

class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = ["level_ID", "img_name"]

class UserDialougeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDialouge
        fields = ["user_dialouge_ID", "npc_ID", "level_ID", "user_input"]

class NPCDialougeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NPCDialouge
        fields = ["npc_dialouge_ID", "npc_ID", "level_ID", "npc_response"]

class NPCsInLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NPCsInLevel
        fields = ["level_ID", "npc_ID"]

class UserGameItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGameItem
        fields = ["item_ID", "item_name"]
