from Parcial_P2 import avengers
nuevos_superheroes = [
    {"superheroe": "q","personaje": "sss","grupo": "sss","aparicion": 2},
    {"superheroe": "w","personaje": "sss","grupo": "sss","aparicion": 2} ,
    {"superheroe": "e","personaje": "sss","grupo": "sss","aparicion": 2},
    {"superheroe": "r","personaje": "sss","grupo": "sss","aparicion": 2} ,
    {"superheroe": "t","personaje": "sss","grupo": "sss","aparicion": 2},
    {"superheroe": "y","personaje": "sss","grupo": "sss","aparicion": 2} ,
    {"superheroe": "u","personaje": "sss","grupo": "sss","aparicion": 2},
    {"superheroe": "i","personaje": "sss","grupo": "sss","aparicion": 2} ,
    {"superheroe": "o","personaje": "sss","grupo": "sss","aparicion": 2},
    {"superheroe": "p","personaje": "sss","grupo": "sss","aparicion": 2} ,
    {"superheroe": "a","personaje": "sss","grupo": "sss","aparicion": 2},
    {"superheroe": "s","personaje": "sss","grupo": "sss","aparicion": 2} ,
    {"superheroe": "d","personaje": "sss","grupo": "sss","aparicion": 2},
    {"superheroe": "f","personaje": "sss","grupo": "sss","aparicion": 2} ,
    {"superheroe": "g","personaje": "sss","grupo": "sss","aparicion": 2},
    {"superheroe": "h","personaje": "sss","grupo": "sss","aparicion": 2} ,
    {"superheroe": "j","personaje": "sss","grupo": "sss","aparicion": 2},
    {"superheroe": "k","personaje": "sss","grupo": "sss","aparicion": 2} ,
    {"superheroe": "l","personaje": "sss","grupo": "sss","aparicion": 2},
    {"superheroe": "ñ","personaje": "sss","grupo": "sss","aparicion": 2} ,
]
for nuevo_superheroe in nuevos_superheroes:
    existe = False
    for personaje in avengers:
        if personaje["superheroe"] == nuevo_superheroe["superheroe"]:
            existe = True
            break
    if not existe:
        avengers.append(nuevo_superheroe)

print("Lista de personajes actualizada:")
for personaje in avengers:
    print(personaje)