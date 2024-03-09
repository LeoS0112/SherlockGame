from django.db import models

# Create your models here.
class NPC(models.Model):
    npc_ID = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100)

class Map(models.Model):
    level_ID = models.AutoField(primary_key = True)

class UserDialouge(models.Model):
    user_dialouge_ID = models.AutoField(primary_key = True)
    npc_ID = models.ForeignKey("NPC", on_delete=models.CASCADE)
    level_ID = models.ForeignKey("Map", on_delete=models.CASCADE)
    user_input = models.TextField()

class NPCDialouge(models.Model):
    npc_dialouge_ID = models.AutoField(primary_key = True)
    npc_ID = models.ForeignKey("NPC", on_delete=models.CASCADE)
    level_ID = models.ForeignKey("Map", on_delete=models.CASCADE)
    npc_response = models.TextField()
   
class NPCsInLevel(models.Model):
    level_ID = models.ForeignKey("Map", on_delete=models.CASCADE)
    npc_ID = models.ForeignKey("NPC", on_delete=models.CASCADE)

class UserGameItem(models.Model):
    item_ID = models.AutoField(primary_key = True)
    item_name = models.CharField(max_length=100)

