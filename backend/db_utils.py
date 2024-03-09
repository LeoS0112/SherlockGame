<<<<<<< HEAD
import requests

endpoint = "https://hidden-fog-37e7f509.zvgz4d.on-acorn.io/"


def add_game_items(item_name : str):
    input = {'item_name': item_name}
    requests.post(endpoint + "user-game-item/", input)

def get_user_response():
    get_response = requests.get(endpoint + "user-dialouge", )
    print(get_response.json())



# def get_list_of_npcs_on_level(level_id, npcs):
#     for npc in npcs:
#         input = {level_id, npc_id}
#         requests.post(endpoint + "npcs-in-level", input)



# get_user_response()
=======
import requests

endpoint = "https://hidden-fog-37e7f509.zvgz4d.on-acorn.io/"


def add_game_items(item_name : str):
    input = {'item_name': item_name}
    requests.post(endpoint + "user-game-item/", input)

def get_user_response():
    get_response = requests.get(endpoint + "user-dialouge", )
    print(get_response.json())

def increment_map_id():
    requests.post(endpoint + "map")

# def get_list_of_npcs_on_level(level_id, npcs: list):
#     # for npc in npcs:
#     print(requests.get(endpoint + "npcs").json())
#     # print(requests.get(endpoint + "npcs-in-level", npc["name"] , headers="npc_ID"))
#     input = {level_id,}
#     requests.post(endpoint + "npcs-in-level", input)

# get_list_of_npcs_on_level(0, [{"name": "fred"}, {"name": "a"}])
>>>>>>> 751eb52016e186c235c9c8e3a55b2986d86f2d64
