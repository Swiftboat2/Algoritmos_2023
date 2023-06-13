from Parcial_P2 import avengers
for personaje in avengers:
    if personaje["superheroe"] == "Vlanck Widow":
            personaje["superheroe"] = "Black Widow"
            break

print("Lista de personajes corregida:")
for personaje in avengers:
    print(personaje)