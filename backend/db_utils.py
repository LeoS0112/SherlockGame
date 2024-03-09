import requests
from time import sleep

endpoint = "https://damp-fog-abf26bfb.zvgz4d.on-acorn.io/"


def add_game_items(item_name : str):
    input = {'item_name': item_name}
    requests.post(endpoint + "user-game-item/", input)

def get_npc(npc_id):
    list_of_dicts = requests.get(endpoint + "npcs").json()
    for all_npc in list_of_dicts:
        if all_npc["npc_ID"] == npc_id:
            return all_npc["name"]

def get_user_response(old_user_input): # Busy wait

    get_response = requests.get(endpoint + "user-dialouge", ).json()


    while get_response[0]["user_input"] == old_user_input[0]["user_input"]:

        sleep(2)

        get_response = requests.get(endpoint + "user-dialouge", ).json()

    return get_response[0]

def add_npc_response(npc_name, level_id, response):
    list_of_dicts = requests.get(endpoint + "npcs").json()
    id = ''
    for all_npc in list_of_dicts:
        if all_npc["name"] == npc_name:
            id = all_npc["npc_ID"]
    requests.post(endpoint + "npc-dialouge/", {"npc_ID": str(id), "level_ID": str(level_id), "npc_response": response})
    get_response = requests.get(endpoint + "user-dialouge").json()
    return get_response

def add_NPC(name : str):
    input = {'name': name}
    requests.post(endpoint + "npcs/", input)

def increment_map_id():
    requests.post(endpoint + "maps/")

def get_list_of_npcs_on_level(level_id, npcs: list):
    npc_id = 0
    get_response = requests.get(endpoint + "npcs")

    print(get_response)

    get_response = get_response.json()

    for all_npc in get_response:
        for npc in npcs:

            if isinstance(npc, dict):
                name = npc["Name"]
            else:
                name = npc.name
            if all_npc["name"] ==  name:
                requests.post(endpoint + "npcs-in-level/", {"level_ID": str(level_id), "npc_ID": str(all_npc["npc_ID"])})

if __name__ == "__main__":
    
    print(get_npc(1))

    

