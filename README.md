
# Elementary: The game

The submission video: https://youtu.be/Iz299y24MXk

**Description:** 

We have built a Sherlock-inspired puzzle game, which is unique in the fact you will have a different experience every time. Using GPT 3.5 and GPT-4 to revolutionize game development by integrating Prolog, a logic programming language, ensuring structure in the simulated world. We used Stability to generate characters based off the name and description of the character. We used prompt engineering to dynamically produce character images, based off the user’s interactions with them. We also made background carpets and the main character avatar. s as referred to in Google's Research into Alpha Geomrtry. We used prolog to prevent hallucinations because Prolog is logical programming language that can provide structure to LLM live user image integration personalizes the experience. With lightweight design and revolutionary concept, we will have a high market impact. We believe we will have a significant industry game-changer with a focus on generative games.

## Frontend

The Game UX is built on UIKit, with each scene built using a separate room UI. The assets for the room are generated on the fly based on the theme, in our case that being Victorian-era London. We liked the 8-bit nostalgic look of the original Pokemon game that was used as the inspiration for Elementary.

## Setup
This will be all ran on bother **Swift** and **Python**
To set up the backend you will need to run the [requirements.txt](/backend/requirements.txt) in the backend folder directory:

```bash
  pip install -r requirements.txt
  pip install openai pyswip
```

You will need to also install:

```bash
scoop install acorn
```

## Running Project

To run the project you will need to run the the [game_items.py](/backend/game_items.py) file and in another terminal run: 

```bash
acorn login
```
Create an account then run:

```bash
acorn dev .
```

you will recieve a link when it start and copy this link into the file [image_uploader.py](/backend/image_uploader.py) in the backend folder: 

```
endpoint = "your link that was generated"
```

## Tech Stack

**Client:** Swift

**Server:** Acorn, AWS

## Authors

- [@ramstar3000](https://www.github.com/ramstar3000)
- [@fred-huang122](https://www.github.com/fred-huang122)
- [@LeoS0112](https://www.github.com/LeoS0112)
- [@aloksahay](https://www.github.com/aloksahay)
