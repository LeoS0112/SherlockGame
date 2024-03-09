import requests

endpoint = "https://damp-fog-abf26bfb.zvgz4d.on-acorn.io/"


def add_game_items(item_name : str):
    input = {'item_name': item_name}
    requests.post(endpoint + "user-game-item/", input)

def get_user_response():
    get_response = requests.get(endpoint + "user-dialouge", )
    print(get_response.json())

def add_npc_response(npc_id, level_id, response):
    input = {"npc_response": response}
    requests.post(endpoint + "npc-dialouge/", input)
    # print(get_response.json())

def add_NPC(name : str):
    input = {'name': name}
    requests.post(endpoint + "npcs/", input)

def increment_map_id():
    requests.post(endpoint + "maps/")

def get_list_of_npcs_on_level(level_id, npcs: list):
    npc_id = 0
    input = {"level_ID": str(level_id), "npc_ID": str(npc_id)}
    get_response = requests.get(endpoint + "npcs").json()
    for all_npc in get_response:
        for npc in npcs:
            if all_npc["name"] ==  npc["name"]:
                requests.post(endpoint + "npcs-in-level/", {"level_ID": str(level_id), "npc_ID": str(all_npc["npc_ID"])})

add_NPC("John")
# add_npc_response("Hello my name is jeff how are you image.")
