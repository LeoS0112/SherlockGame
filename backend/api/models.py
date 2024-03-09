from django.db import models

# Create your models here.
class NPC(models.Model):
    npc_ID = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=100)

class Map(models.Model):
    level_ID = models.IntegerField(primary_key = True)

class Conversations(models.Model):
    conversation_ID = models.IntegerField(primary_key = True)
    npc_ID = models.ForeignKey("NPC", on_delete=models.CASCADE)
    level_ID = models.ForeignKey("Map", on_delete=models.CASCADE)
    last_conversation = models.TextField()
    npc_response = models.TextField()
    user_input = models.TextField()
    timestamp = models.DateTimeField()
   
class NPCsInLevel(models.Model):
    level_ID = models.ForeignKey("Map", on_delete=models.CASCADE)
    npc_ID = models.ForeignKey("NPC", on_delete=models.CASCADE)

class UserGameItem(models.Model):
    item_ID = models.IntegerField(primary_key = True)
    item_name = models.CharField(max_length=100)

