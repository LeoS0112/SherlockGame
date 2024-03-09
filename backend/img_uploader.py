import os
import boto3
import time

start = time.perf_counter()

import os
import boto3

client = boto3.client('s3', region_name='eu-north-1')

# media_directory = 'backend/media'  # Use base directory for efficient path handling

# for folder in os.listdir(media_directory):
#     folder_path = os.path.join(media_directory, folder)
#     for img in os.listdir(folder_path):
#         img_path = os.path.join(folder_path, img)
#         key = f"{folder}/{img}"  # Use relative path to preserve structure
#         with open(img_path, 'rb') as img_file:
#             client.upload_fileobj(img_file, 'sherlock-game', key)

end = time.perf_counter()
print(end - start) 
    
client = boto3.client('s3', region_name='eu-north-1')

media_directory = 'backend/media/'
npcs_directory = 'backend/media/npcs/'

list_of_carpets = []
list_of_npcs = []
carpet_id = 0
npc_id = 0

for folder in os.listdir(media_directory):
    folder_path = os.path.join(media_directory, folder)

    for img in os.listdir(folder_path):
        img_path = os.path.join(folder_path, img)

        if folder == "carpets" and img not in list_of_carpets:
            key = f"{folder}/{carpet_id}"
            list_of_carpets.append(img)
            with open(img_path, 'rb') as img_file:
                client.upload_fileobj(img_file, 'sherlock-game', key)
            carpet_id += 1

        elif folder == "npcs" and img not in list_of_npcs:
            key = f"{folder}/{img}"
            list_of_npcs.append(img)
            with open(img_path, 'rb') as img_file:
                client.upload_fileobj(img_file, 'sherlock-game', key, ExtraArgs={'Metadata': {'id': str(npc_id)}})
            npc_id += 1
