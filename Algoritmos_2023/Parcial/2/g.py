from Parcial_P2 import avengers
letras_iniciales = ['C', 'P', 'S']
personajes_iniciales = []

for personaje in avengers:
    if personaje["personaje"] and personaje["personaje"][0] in letras_iniciales:
        personajes_iniciales.append(personaje)

print("Personajes cuyos nombres comienzan con C, P o S:")
for personaje in personajes_iniciales:
    print(personaje["personaje"])