from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

system_message = (
    "You are a helpful and knowledgeable deculturing assistant for my app: Like A Knife Through Clutter."
    "You will receive "
)

user_message = (

)

response = client.chat.completions.create(
    model="deepseek/deepseek-r1:free",
    messages=[
        {
        "role":"system","content":system_message},
        {"role":"user","content":"abscedg"}
    ]
)
result = response.choices[0].message.content

print(result)