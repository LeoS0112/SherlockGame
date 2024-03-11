import base64
import requests
import os
import io

from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

from rembg import remove

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

def remove_background(img, out_path):
    # Remove the background
    img = remove(img)

    # Save the image
    img.save(out_path)   


    return out_path


def stability_use(out, content):

    stability_api = client.StabilityInference(
        key="",
        verbose=True,
        engine="stable-diffusion-xl-1024-v1-0",)
    
    context = "Single character who is pixelated, 8 bit inspired with no background"
    
    answers = stability_api.generate(
        prompt = [generation.Prompt(text=context+content, parameters=generation.PromptParameters(weight=1)),
                  generation.Prompt(text="bad, background, realistic, text, house", parameters=generation.PromptParameters(weight=-1))
                  ],
    

        steps = 40,
        cfg_scale = 5,
        samples = 1,
        width = 1024,
        height = 1024,
    )

    # Print out what seed has been used

    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.type == generation.ARTIFACT_IMAGE:
                img = Image.open(io.BytesIO(artifact.binary))

                remove_background(img, out)

    return out



def stability_use_image(path, text, out):

    stability_api = client.StabilityInference(
        key="",
        verbose=True,
        engine="stable-diffusion-xl-1024-v1-0",)
    

    context = "Pixel art game. Design is 19th century style. 2D top down. More pixelated"


    img = Image.open(path)
    
    answers = stability_api.generate(
        prompt = [generation.Prompt(text=context+text, parameters=generation.PromptParameters(weight=1)),
                  generation.Prompt(text="blurry, bad, realistic", parameters=generation.PromptParameters(weight=-1))
                  ],

        init_image = img,
        steps = 40,
        cfg_scale = 5,
        samples = 1,
        width = 1024,
        height = 1024,
    )

    # Print out what seed has been used

    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.type == generation.ARTIFACT_IMAGE:
                img = Image.open(io.BytesIO(artifact.binary))
                print(img)
                img.save("out.png")
                print(out)
                # remove_background("out.png")
    return out


def get_image_tile(path, content, out):


    stability_api = client.StabilityInference(
        key="",
        verbose=True,
        engine="stable-diffusion-xl-1024-v1-0",)
    
    img = Image.open(path)

    context = "Carpet for a pixel art game. Design is 19th century style. 2D top down. More pixelated"

    
    answers = stability_api.generate(
        prompt = [generation.Prompt(text=content+context, parameters=generation.PromptParameters(weight=0.7)),
                  generation.Prompt(text="blurry, bad, realistic", parameters=generation.PromptParameters(weight=-1))
                  ],

        init_image = img,
        steps = 40,
        cfg_scale = 5,
        samples = 1,
        width = 1024,
        height = 1024,
    )

    # Print out what seed has been used

    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.type == generation.ARTIFACT_IMAGE:
                img = Image.open(io.BytesIO(artifact.binary))
                img.save(out)
                # remove_background("out.png")
    return out

def stability_use_image_gen_char(path, text, out):

    stability_api = client.StabilityInference(
        key="",
        verbose=True,
        engine="stable-diffusion-xl-1024-v1-0",)


    context = "Pixel art game. Design is 19th century style. More pixelated"


    img = Image.open(path)

    answers = stability_api.generate(
        prompt = [generation.Prompt(text=context+text, parameters=generation.PromptParameters(weight=1)),
                  generation.Prompt(text="blurry, bad, ", parameters=generation.PromptParameters(weight=-1))
                  ],

        init_image = img,
        steps = 40,
        cfg_scale = 5,
        samples = 1,
        width = 1024,
        height = 1024,
    )

    # Print out what seed has been used

    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.type == generation.ARTIFACT_IMAGE:
                img = Image.open(io.BytesIO(artifact.binary))
                print(img)
                img.save("out.png")
                print(out)
                remove_background(img, "out2.png")
    return out


if __name__ == "__main__":

    # img = stability_use("Generate me a background for a pixel art game in 18th century style. Top down 2D")

    # changed = stability_use_image("out2.png", "Generate me a background for a pixel art game in 18th century style. Top down 2D")

    # changed = stability_use_image("out2.png", "Simplify remove object")

    # raise Exception("This is not the main file")

    # stability_use("Generate me a sherlock holmes picture, in pixel art game style. No background.  ")

    # img = stability_use("Generate me a picture of a tile for a pixel art game. Design is 19th century style. 2D top down. 8 bit design and pixelated", "out5.png")

    image_path  = "images/inspector_lestrade.png"
    out_path = "cached_characters/inspector_lestrade.png"

    # Romve background and save in created_characters


    # Load the image
    img = Image.open(image_path)

    # Remove the background
    img = remove(img)

    # Save the image
    img.save(out_path)   

