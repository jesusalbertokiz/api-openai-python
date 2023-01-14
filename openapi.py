"""Module providingFunction printing python version."""
import openai

KEY = "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"
openai.api_key = KEY

question = input("Pregunta: ")


completion = openai.Completion.create(engine="text-davinci-003", prompt=question, max_tokens=500, temperature=0.9, top_p=1, frequency_penalty=0, presence_penalty=0.6)

text = completion.choices[0].text
text = text.replace("   ", " ")     

text = text.encode('latin-1').decode('unicode_escape')
print(text)



