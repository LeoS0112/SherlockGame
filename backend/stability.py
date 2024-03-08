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
            {"text": f"{text}", "weight": 1},
            {"text": "blurry, bad, background, realistic", "weight": -1},
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


def stability_use(text, out):
    stability_api = client.StabilityInference(
        key="sk-NHyorRj8N5c2xvbOeLdsXHuYO7RWoG7oXufqhmX2g00o7pB6",
        verbose=True,
        engine="stable-diffusion-xl-1024-v1-0",
    )

    answers = stability_api.generate(
        prompt=[
            generation.Prompt(
                text=text, parameters=generation.PromptParameters(weight=1)
            ),
            # generation.Prompt(text="blurry, bad, background, realistic", parameters=generation.PromptParameters(weight=-1))
        ],
        steps=40,
        cfg_scale=5,
        samples=1,
        width=1024,
        height=1024,
    )

    # Print out what seed has been used

    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.type == generation.ARTIFACT_IMAGE:
                img = Image.open(io.BytesIO(artifact.binary))
                img.show()
                img.save(out)

    return out


def remove_background(image_path):
    # Load the image
    img = Image.open(image_path)

    # Remove the background
    img = remove(img)

    # Save the image
    img.save("out.png")

    return "out.png"


def stability_use_image(path, text, out):
    stability_api = client.StabilityInference(
        key="sk-NHyorRj8N5c2xvbOeLdsXHuYO7RWoG7oXufqhmX2g00o7pB6",
        verbose=True,
        engine="stable-diffusion-xl-1024-v1-0",
    )

    img = Image.open(path)

    answers = stability_api.generate(
        prompt=[
            generation.Prompt(
                text=text, parameters=generation.PromptParameters(weight=0.7)
            ),
            generation.Prompt(
                text="blurry, bad, realistic",
                parameters=generation.PromptParameters(weight=-1),
            ),
        ],
        init_image=img,
        steps=40,
        cfg_scale=5,
        samples=1,
        width=1024,
        height=1024,
    )

    # Print out what seed has been used

    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.type == generation.ARTIFACT_IMAGE:
                img = Image.open(io.BytesIO(artifact.binary))
                img.show()
                img.save(out)
                # remove_background("out.png")
    return out


if __name__ == "__main__":
    # img = stability_use("Generate me a background for a pixel art game in 18th century style. Top down 2D")

    # changed = stability_use_image("out2.png", "Generate me a background for a pixel art game in 18th century style. Top down 2D")

    # changed = stability_use_image("out2.png", "Simplify remove object")

    # raise Exception("This is not the main file")

    # stability_use("Generate me a sherlock holmes picture, in pixel art game style. No background.  ")

    img = stability_use(
        "Generate me a picture of a tile for a pixel art game. Design is 19th century style. 2D top down. 8 bit design and pixelated",
        "out5.png",
    )

    print(img)

    stability_use_image(
        img,
        "Generate me a complimentary picture of a carpet for a pixel art game. Design is 19th century style. 2D top down. More pixelated",
        out="out6.png",
    )
