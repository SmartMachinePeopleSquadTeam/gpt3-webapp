import openai
import os

def summarize_with_gpt3(text):
    tldr_tag = "\n tl;dr:"
    prompt = text + tldr_tag
    openai.api_key = os.environ['openai-key']
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.3,
        max_tokens=140,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"],
    )
    return response