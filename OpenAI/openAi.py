import openai

Questions = input("Enter your Question: ")

openai.api_key = "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"

response = openai.Completion.create(
    model="text-davinci-002",
    prompt=Questions,
    temperature=1,
    max_tokens=150,
    top_p=1,
    frequency_penalty=2,
    presence_penalty=2,
    stop=[" Human:", " AI:"]
)
answer = response.choices[0].text
print(answer)