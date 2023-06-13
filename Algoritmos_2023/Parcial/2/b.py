from Parcial_P2 import avengers
from collections import deque
cola_guardianes = deque()
cantidad_guardianes = 0

for personaje in avengers:
    if personaje["grupo"] == "Guardianes de la galaxia":
        cola_guardianes.append(personaje["superheroe"])
        cantidad_guardianes += 1

print(f"Los superhéroes que pertenecen al grupo 'Guardianes de la galaxia' son:")
for superheroe in cola_guardianes:
    print(superheroe)

print(f"La cantidad de superhéroes en el grupo 'Guardianes de la galaxia' es: {cantidad_guardianes}")