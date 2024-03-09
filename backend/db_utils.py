import requests

endpoint = "https://hidden-fog-37e7f509.zvgz4d.on-acorn.io/"


def add_game_items(item_name : str):
    input = {'item_name': item_name}
    requests.post(endpoint + "user-game-item", input)

def get_user_response():
    get_response = requests.get(endpoint + "user-game-item", )
    print(get_response.json())



# def get_list_of_npcs_on_level(level_id, npcs):
#     for npc in npcs:
#         input = {level_id, npc_id}
#         requests.post(endpoint + "npcs-in-level", input)



get_user_response()