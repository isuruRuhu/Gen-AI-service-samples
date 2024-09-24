# sample to test openai api
import openai
import os
from openai import OpenAI
client = OpenAI()

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_chat_completions(messages):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": messages}
            ]
        )

        # Extract and return the generated text
        return completion.choices[0].message

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    while True:
        user_prompt = input("Enter a prompt (or type 'exit' to quit): ")
        if user_prompt.lower() == 'exit':
            break
        output = get_chat_completions(user_prompt)
        print("Generated Text:", output.content)
