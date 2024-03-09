from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import NPC, Map, UserDialouge, NPCDialouge, NPCsInLevel, UserGameItem
from .serializers import NPCSerializer, MapSerializer, UserDialougeSerializer, NPCDialougeSerializer, NPCsInLevelSerializer, UserGameItemSerializer

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

# UserDialouge CRUD
class UserDialougeListCreate(generics.ListCreateAPIView):
    queryset = UserDialouge.objects.all()
    serializer_class = UserDialouge

    def delete(self, request, *args, **kwargs):
        UserDialouge.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserDialougeRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserDialouge.objects.all()
    serializer_class = UserDialouge
    lookup_field = "pk"
    
# NPCDialouge CRUD
class NPCDialougeListCreate(generics.ListCreateAPIView):
    queryset = NPCDialouge.objects.all()
    serializer_class = NPCDialougeSerializer

    def delete(self, request, *args, **kwargs):
        NPCDialouge.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NPCDialougeRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = NPCDialouge.objects.all()
    serializer_class = NPCDialougeSerializer
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
