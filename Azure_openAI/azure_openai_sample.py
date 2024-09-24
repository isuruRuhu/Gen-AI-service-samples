import os
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key="Your Azure OpenAI API Key",
    api_version="2024-02-01",
    azure_endpoint="Your Azure OpenAI Endpoint"
)

deployment_name = 'Your deployment name goes here'


def get_chat_completions(messages):
    try:
        completion = client.chat.completions.create(
            model=deployment_name,
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
