from openai import OpenAI


def generate_response_gpt(prompt, key=None):

    if key is None:
        file = open("backend/secret.txt", "r")
        key = file.read()
        file.close()

    client = OpenAI(api_key=key)

    context = ""

    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": context + prompt}],
        stream=True,
    )
    response = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            response += chunk.choices[0].delta.content

    return response

if __name__ == "__main__":

    prompt = "What is the meaning of life?"
    print(generate_response_gpt(("user", prompt)))
