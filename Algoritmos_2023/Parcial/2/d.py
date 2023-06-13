from Parcial_P2 import avengers
superheroes_post_1960 = []

for personaje in avengers:
    if personaje["personaje"] != "" and personaje["aparicion"] > 1960:
        superheroes_post_1960.append(personaje["superheroe"])

print("Superhéroes con nombre de personaje cuyo año de aparición es posterior a 1960:")
for heroe in superheroes_post_1960:
    print(heroe)