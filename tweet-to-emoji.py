"""
Con este modelo se usa GPT-3 para generar un emoji a partir de un tweet (texto).
"""

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

restart_sequence = "###\n"

response = openai.Completion.create(
    engine="davinci",
    prompt='This is a tweet to emoji converter.\n\nTweet: "I loved the new Batman movie!"\nEmoji: ๐๐ฆ\n###\nTweet: "I hate it when my phone battery dies."\nEmoji: ๐คฌ๐ต\n###\nTweet: "Tengo mucha hambre, me comerรญa un caballo entero"\nEmoji: ๐๐\n###\nTweet: "This is the link to the article"\nEmoji: ๐ฒ๐\n###\nTweet: "This new music video blew my mind"\nEmoji: ๐ฎ๐ฅ\n###\nTweet: "And the stars look very different today."\nEmoji: ๐๐ \n###\nTweet: "Coconut water taste like itโs been in someone elseโs mouth"\nEmoji: ๐คข๐ฐ๐ฅฅ\n###\nTweet: "Iโm going to the gym to work out"\nEmoji: ๐๐ป๐ช\n###\nTweet: "En unas horas viajo de nuevo a Polonia con mis educandos."\nEmoji: ๐๐๐\n###\nTweet: "Iโm going to miss this place."\nEmoji: ๐๐ท\n###\n',
    temperature=0.41,
    max_tokens=82,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0,
    stop=["###"],
)
