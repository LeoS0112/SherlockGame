from django.shortcuts import render
from rest_framework import generics
from .models import NPC
from .serializers import NPCSerializer

class NPCListCreate(generics.ListCreateAPIView):
    queryset = NPC.objects.all()
    serializer_class = NPCSerializer