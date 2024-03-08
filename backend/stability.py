import base64
import requests
import os
import io

from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation


# Need to usee stability for
    # Creating tile maps for rooms
    # Character designs
    # Potentially objects

def stability_example(text: str = "A picture of a cat"): 

    url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"

    body = {
    "steps": 40,
    "width": 1024,
    "height": 1024,
    "seed": 0,
    "cfg_scale": 5,
    "samples": 1,
    "text_prompts": [
        {
        "text": f"{text}",
        "weight": 1
        },
        {
        "text": "blurry, bad, background, realistic",
        "weight": -1
        }
    ],
    }

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer sk-NHyorRj8N5c2xvbOeLdsXHuYO7RWoG7oXufqhmX2g00o7pB6",
    }

    response = requests.post(
    url,
    headers=headers,
    json=body,
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()

    # make sure the out directory exists
    if not os.path.exists("./out"):
        os.makedirs("./out")

    for i, image in enumerate(data["artifacts"]):
        with open(f'./out/txt2img_{image["seed"]}.png', "wb") as f:
            f.write(base64.b64decode(image["base64"]))



def stability_use(text):

    stability_api = client.StabilityInference(
        key="sk-NHyorRj8N5c2xvbOeLdsXHuYO7RWoG7oXufqhmX2g00o7pB6",
        verbose=True,
        engine="stable-diffusion-xl-1024-v1-0",)
    
    answers = stability_api.generate(
        prompt=text,
        # return_prompt=True,
        # return_input=True,
        # return_score=True,
        # return_artifacts=True,
        # return_logprobs=True,
        # return_trace=True,
        # return_attention=True,
        seed = 121245125,
        steps = 30,
        cfg_scale = 5,
        samples = 1,
        width = 1024,
        height = 1024,
        # Sample  = ...
    )

    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.type == generation.ARTIFACT_IMAGE:
                img = Image.open(io.BytesIO(artifact.binary))
                img.show()





if __name__ == "__main__":
    stability_use("Generate me a sherlock holmes picture, in pixel art game style. Make sure it is only him. Blank background.  ")