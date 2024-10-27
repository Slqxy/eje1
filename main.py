meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobación",
            "CREEPY": "aterrador, siniestro",
            "AGGRO": "ponerse agresivo/enojado"
            }

print("Hola, bienvenido")

for i in range(5):
    word = input("\nEscribe una palabra que no entiendas (¡con mayúsculas!): ")

    if word in meme_dict.keys():
        # ¿Qué debemos hacer si se encuentra la palabra?
        print(word, "Significa:", meme_dict[word])
    else:
        # ¿Qué hacer si no se encuentra la palabra?
        print("Lo siento, no existe la palabra")
