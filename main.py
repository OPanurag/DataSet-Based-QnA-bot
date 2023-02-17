# export OPENAI_API_KEY="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"

import openai

openai.api_key ="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"

prompt = '{}'.format(input('Please enter a command --> '))

response = openai.Completion.create(
    model='davinci:ft-personal-2023-02-16-22-14-51',
    prompt=prompt,
    temperature=0,
    max_tokens=100)

print(response)
