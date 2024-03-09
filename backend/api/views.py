from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import NPC, Map, Conversations, NPCsInLevel, UserGameItem
from .serializers import NPCSerializer, MapSerializer, ConversationsSerializer, NPCsInLevelSerializer, UserGameItemSerializer

# NPC CRUD
class NPCListCreate(generics.ListCreateAPIView):
    queryset = NPC.objects.all()
    serializer_class = NPCSerializer

    def delete(self, request, *args, **kwargs):
        NPC.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NPCRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = NPC.objects.all()
    serializer_class = NPCSerializer
    lookup_field = "pk"

#Map CRUD
class MapListCreate(generics.ListCreateAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer

    def delete(self, request, *args, **kwargs):
        Map.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MapRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer
    lookup_field = "pk"

# Conversation CRUD
class ConversationListCreate(generics.ListCreateAPIView):
    queryset = Conversations.objects.all()
    serializer_class = ConversationsSerializer

    def delete(self, request, *args, **kwargs):
        Conversations.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ConversationsRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Conversations.objects.all()
    serializer_class = ConversationsSerializer
    lookup_field = "pk"

# NPCsInLevel CRUD
    
class NPCsInLevelListCreate(generics.ListCreateAPIView):
    queryset = NPCsInLevel.objects.all()
    serializer_class = NPCsInLevelSerializer

    def delete(self, request, *args, **kwargs):
        NPCsInLevel.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NPCsInLevelRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = NPCsInLevel.objects.all()
    serializer_class = NPCsInLevelSerializer
    lookup_field = "pk"

# UserGameItem CRUD
class UserGameItemListCreate(generics.ListCreateAPIView):
    queryset = UserGameItem.objects.all()
    serializer_class = UserGameItemSerializer

    def delete(self, request, *args, **kwargs):
        UserGameItem.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserGameItemRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserGameItem.objects.all()
    serializer_class = UserGameItemSerializer
    lookup_field = "pk"

