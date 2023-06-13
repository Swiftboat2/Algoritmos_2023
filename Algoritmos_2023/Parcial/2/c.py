from Parcial_P2 import avengers
superheroes_cuatro_fantasticos = []
superheroes_guardianes_galaxia = []

for personaje in avengers:
    if personaje["grupo"] == "Los cuatro fantásticos":
        superheroes_cuatro_fantasticos.append(personaje["superheroe"])
    elif personaje["grupo"] == "Guardianes de la galaxia":
        superheroes_guardianes_galaxia.append(personaje["superheroe"])

superheroes_cuatro_fantasticos.sort(reverse=True)
superheroes_guardianes_galaxia.sort(reverse=True)

print("Superhéroes del grupo 'Los cuatro fantásticos' (orden descendente):")
for heroe in superheroes_cuatro_fantasticos:
    print(heroe)

print("\nSuperhéroes del grupo 'Guardianes de la galaxia' (orden descendente):")
for heroe in superheroes_guardianes_galaxia:
    print(heroe)