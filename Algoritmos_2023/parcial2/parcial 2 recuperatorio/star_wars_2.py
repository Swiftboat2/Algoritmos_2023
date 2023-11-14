from grafo import Grafo


grafo = Grafo()

#A-D
grafo.insert_vertice('Luke Skywalker')
grafo.insert_vertice('Darth Vader')
grafo.insert_vertice('Kylo Ren')
grafo.insert_vertice('Leia')
grafo.insert_vertice('Boba Fett')
grafo.insert_vertice('C-3PO')
grafo.insert_vertice('Rey')
grafo.insert_vertice('Chewbacca')
grafo.insert_vertice('Han Solo')
grafo.insert_vertice('R2-D2')
grafo.insert_vertice('BB-8')
grafo.insert_vertice('Yoda')


grafo.insert_arist('Luke Skywalker', 'Darth Vader', 5)
grafo.insert_arist('Luke Skywalker', 'Kylo Ren', 2)
grafo.insert_arist('Luke Skywalker', 'Leia', 3)
grafo.insert_arist('Darth Vader', 'Kylo Ren', 4)
grafo.insert_arist('Darth Vader', 'Leia', 2)
grafo.insert_arist('Kylo Ren', 'Leia', 1)
grafo.insert_arist('Leia', 'Boba Fett', 3)
grafo.insert_arist('Leia', 'C-3PO', 4)
grafo.insert_arist('Leia', 'Rey', 5)
grafo.insert_arist('Boba Fett', 'C-3PO', 2)
grafo.insert_arist('Boba Fett', 'Rey', 1)
grafo.insert_arist('C-3PO', 'Rey', 3)
grafo.insert_arist('Chewbacca', 'Han Solo', 4)
grafo.insert_arist('R2-D2', 'BB-8', 2)
grafo.insert_arist('Yoda', 'Chewbacca', 1)


#B
arbol_expansion_minimo = grafo.kruskal()

print('Árbol de Expansión Mínimo:')
for arista in arbol_expansion_minimo:
    print(arista)

contiene_yoda = False
for arista in arbol_expansion_minimo:
    if 'Yoda' in arista:
        contiene_yoda = True
        break

if contiene_yoda:
    print('El árbol de expansión mínimo contiene a Yoda.')
else:
    print('El árbol de expansión mínimo no contiene a Yoda.')

#C

def encontrar_max_episodios_compartidos(grafo):
        max_episodios = 0
        personajes_con_max_episodios = []

        for personaje, relaciones in grafo.grafo.items():
            for relacion in relaciones:
                otro_personaje, episodios = relacion
                if episodios > max_episodios:
                    max_episodios = episodios
                    personajes_con_max_episodios = [(personaje, otro_personaje)]
                elif episodios == max_episodios:
                    personajes_con_max_episodios.append((personaje, otro_personaje))

                    return max_episodios, personajes_con_max_episodios
                
max_episodios, personajes_con_max_episodios = encontrar_max_episodios_compartidos(grafo)

print(f"Número máximo de episodios compartidos: {max_episodios}")
print("Personajes que comparten este número de episodios:")
for personaje1, personaje2 in personajes_con_max_episodios:
    print(f"{personaje1} y {personaje2}")

if not personajes_con_max_episodios:
    print('No se encontraron personajes que compartan episodios.')

#Punto recuperatorio
ori = 'yoda'
fina = 'rey'
origen = grafo.search_vertice(ori)
final = grafo.search_vertice(fina)
camino_mas_corto = None

if origen is not None and final is not None:
    if grafo.has_path(ori, fina):
        camino_mas_corto = grafo.dijkstra(ori, fina)
        fin = fina
        while camino_mas_corto.size() > 0:
            value = camino_mas_corto.pop()
            if fin == value[0]:
                print(value[0], value[1])
                fin = value [2]