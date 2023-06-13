from Parcial_P2 import avengers
lista_auxiliar = [
    {"superheroe": "Black Cat","personaje": "Felicia Hardy","grupo": "Black Cat's Gang","aparicion": 1979},
    {"superheroe": "Hulk", "personaje": "Bruce Banner","grupo": "Avengers","aparicion": 1962},
    {"superheroe": "Rocket Racoonn","personaje": "89P13 ","grupo": "Guardianes de la galaxia","aparicion": 1976},
    {"superheroe": "Loki","personaje": "Loki Laufeyson","grupo": "Familia Real Asgardiana","aparicion": 1949}
]

for personaje_auxiliar in lista_auxiliar:
    existe = False
    for personaje in avengers:
        if personaje["superheroe"] == personaje_auxiliar:
            existe = True
            break
    if not existe:
        nuevo_personaje = {
            "superheroe": personaje_auxiliar,
            "personaje": "",  
            "grupo": "",  
            "aparicion": 0
        }
        avengers.append(nuevo_personaje)

print("Lista de personajes actualizada:")
for personaje in avengers:
    print(personaje)