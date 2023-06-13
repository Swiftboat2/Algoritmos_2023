from Parcial_P2 import avengers
personaje_buscado = "Capitana Marvel"
nombre_personaje = None

for personaje in avengers:
    if personaje["superheroe"] == personaje_buscado:
        nombre_personaje = personaje["personaje"]
        break
if nombre_personaje:
    print(f"El nombre de personaje de '{personaje_buscado}' es: {nombre_personaje}")
else:
    print(f"No se encontró el personaje '{personaje_buscado}' en la lista.")