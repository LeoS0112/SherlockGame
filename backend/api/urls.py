from django.urls import path
from . import views

urlpatterns = [
    path("npcs/", views.NPCListCreate.as_view(), name="npc-view-create"),
    path("npcs/<int:pk>/", views.NPCRetrieveUpdateDestory.as_view(), name="npc-retrieve-update-destroy"),
    path("maps/", views.MapListCreate.as_view(), name="map-view-create"),
    path("maps/<int:pk>/", views.MapRetrieveUpdateDestory.as_view(), name="map-retrieve-update-destroy"),
    path("user-dialouge/", views.UserDialougeListCreate.as_view(), name="usr-dia-view-create"),
    path("user-dialouge/<int:pk>/", views.UserDialougeRetrieveUpdateDestory.as_view(), name="user-dia-retrieve-update-destroy"),
    path("npc-dialouge/", views.NPCDialougeListCreate.as_view(), name="npc-dia-view-create"),
    path("npc-dialouge/<int:pk>/", views.NPCDialougeRetrieveUpdateDestory.as_view(), name="npc-dia-retrieve-update-destroy"),
    path("npcs-in-level/", views.NPCsInLevelListCreate.as_view(), name="npc-in-level-view-create"),
    path("npcs-in-level/<int:pk>/", views.NPCsInLevelRetrieveUpdateDestory.as_view(), name="npcs-in-level-retrieve-update-destroy"),
    path("user-game-item/", views.UserGameItemListCreate.as_view(), name="user-game-item-view-create"),
    path("user-game-item/<int:pk>/", views.UserGameItemRetrieveUpdateDestory.as_view(), name="user-game-item-retrieve-update-destroy"),
]
