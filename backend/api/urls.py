from django.urls import path
from . import views

urlpatterns = [
    path("npcs/", views.NPCListCreate.as_view(), name="npc-view-create"),
    path("npcs/<int:pk>/", views.NPCRetrieveUpdateDestory.as_view(), name="npc-retrieve-update-destroy"),
    path("maps/", views.MapListCreate.as_view(), name="map-view-create"),
    path("maps/<int:pk>/", views.MapRetrieveUpdateDestory.as_view(), name="map-retrieve-update-destroy"),
    path("conversations/", views.ConversationListCreate.as_view(), name="conv-view-create"),
    path("conversations/<int:pk>/", views.NPCRetrieveUpdateDestory.as_view(), name="conv-retrieve-update-destroy"),
    path("npcs-in-level/", views.MapListCreate.as_view(), name="npc-in-level-view-create"),
    path("npcs-in-level/<int:pk>/", views.MapRetrieveUpdateDestory.as_view(), name="npcs-in-level-retrieve-update-destroy"),
    path("user-game-item/", views.MapListCreate.as_view(), name="user-game-item-view-create"),
    path("user-game-item/<int:pk>/", views.MapRetrieveUpdateDestory.as_view(), name="user-game-item-retrieve-update-destroy"),
]
