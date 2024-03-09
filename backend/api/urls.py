from django.urls import path
from . import views

urlpatterns = [
    path("npcs/", views.NPCListCreate.as_view(), name="npc-view-create")
]
