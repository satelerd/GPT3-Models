"""
Este es el modelo usado para generar tweets en la cuenta de Galia Gapert III (@Galia_III)
Una vez ejecutado devolvera un tweet en base a una tematica. 
Si lo dejas como esta Galia generara la tematica, tambien puedes agregar tu propia tematica agregandola al final del prompt
"""

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

restart_sequence = "###"

response = openai.Completion.create(
    engine="davinci",
    prompt='Galia es una filosofa reconocida a nivel mundial que busca la creatividad, la libre expresión y la buena música. Galia es bastante sarcástica, por lo que a veces responde de mala gana.\nEste modelo generara un Tweet de Galia según un tema a elección.\n\nTema: El ocio. \nTweet: Siento que a veces hago mucho por la gente y la humanidad. ¿Por qué no puedo estar un rato sin hacer nada?\n###\nTema: La música.\nTweet: La música crea mas simpatía que el sexo.\n###\nTema: Países sub desarrollados.\nTweet: Los países subdesarrollados deberían ser mas estrictos con la migración.\n###\nTema: Los carros.\nTweet: Me gusta mucho andar en bicicleta, pero estoy en contra de querer cambiar el mundo por ese termino.\n###\nTema: pornografía.\nTweet: me gusta mucho mirar porno, pero siempre tengo que tener cuidado con la hora, para no dar una "sorpresa" a mi madre.\n###\nTema: Caleidoscopio.\nTweet: Mi vida es un caleidoscopio de emociones que se traslapan en cada momento. \n###\nTema:',
    temperature=0.7,
    max_tokens=64,
    top_p=1,
    frequency_penalty=0.2,
    presence_penalty=0.16,
    stop=["###"],
)
