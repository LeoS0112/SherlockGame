import requests

endpoint = "https://damp-fog-abf26bfb.zvgz4d.on-acorn.io/"


def add_game_items(item_name : str):
    input = {'item_name': item_name}
    requests.post(endpoint + "user-game-item/", input)

def get_user_response():
    get_response = requests.get(endpoint + "user-dialouge", )
    print(get_response.json())

def increment_map_id():
    requests.post(endpoint + "map")

def get_list_of_npcs_on_level(level_id, npcs: list):
    print("=====================================")
    npc_id = 0
    print(npcs)
    print(type(npcs))
    print(type(npcs[0]))
    get_response = requests.get(endpoint + "npcs").json()
    for all_npc in get_response:
        for npc in npcs:

            if isinstance(npc, dict):
                name = npc["Name"]
            else:
                name = npc.name
            

            if all_npc["name"] ==  name:
                print({"level_ID": str(level_id), "npc_ID": str(all_npc["npc_ID"])})
                requests.post(endpoint + "npcs-in-level/", {"level_ID": str(level_id), "npc_ID": str(all_npc["npc_ID"])})
            


# get_list_of_npcs_on_level(1, [{"name": "fred"}, {"name": "a"}])
