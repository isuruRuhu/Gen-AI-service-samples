import os
from openai import AzureOpenAI

# client = AzureOpenAI(
#   api_key = os.getenv("AZURE_OPENAI_API_KEY"),
#   api_version = "2024-06-01",
#   azure_endpoint =os.getenv("AZURE_OPENAI_ENDPOINT")
# )

deployment_name = "Your deployment name goes here"

client = AzureOpenAI(
    api_key="Your Azure OpenAI API Key",
    api_version="2024-06-01",
    azure_endpoint="Your Azure OpenAI Endpoint"
)

response = client.embeddings.create(
    input="Your text string goes here",
    model=deployment_name
)

print(response.model_dump_json(indent=2))
