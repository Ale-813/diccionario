meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "CUTE": "Algo adorable, o tierno",
    "XD": "Un emoji de risa",  
    "IDK": "I DON'T KNOW: No sé"
}

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict:
    print(meme_dict[word])
else:
    print("La palabra no existe :(")
