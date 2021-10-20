"""
Este modelo fue entrenado con distintas frases de canciones de las distintas bandas de Spinetta.
Una vez ejecutado devolvera una frase completamente nueva.
"""

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
    engine="davinci",
    prompt="Lo siguiente es un generador de frases de Spinetta.\n\n- La distancia es un caudal de eternidad, agazapada sobre la espalda de un león.\n- Y entre los libros de la buena memoria, se queda oyendo como un ciego frente al mar.\n- ¿Qué sombra extraña te ocultó de mi guiño? Que nunca oíste la hojarasca crepitar.\n- Los ojos de los miles, se te encienden como velas entre los luceros.\n- Habrá crecido un tallo en el nogal, La luz habrá tiznado gente sin fe\n- Las parres tienen aliento y apadrinan confesiones habitables\n- El club de la montaña sagrada es lugar incognito, sus reglas son inescrutables\n- Árbol, hoja, salto, luz. Nube, loba, dedo, cal, gesticulador.\n- En la aspereza de tu mirada te contrapone el zorro\n- Agazapados bajo el umbral; la montaña acoge a todo viajero.\n- El viento gira en la aurora, al pisar los pliegues del sueño entrevero tu huella.\n- Venas enrojecidas por fiebres del ris y cadenas muertas de Lorca.\n- El rencor es un cazador abrigado bajo los huecos de la pobre memoria\n- La noche élfica me persigue como copas en el sueño.\n- El ala del idioma se parte y el pájaro brota.\n- La luz ciega mientras el juglar persigue un sonido redondo, era una sombra de noche\n- Spinetta pernoctó por su tierra y encontró el oro perdido.",
    temperature=1,
    max_tokens=20,
    top_p=1,
    frequency_penalty=1.48,
    presence_penalty=1.36,
)
