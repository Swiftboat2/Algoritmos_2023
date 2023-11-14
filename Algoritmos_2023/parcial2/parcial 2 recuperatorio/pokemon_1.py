from arbol_binario import BinaryTree

pokemon_list = [
    {"nombre": "Pikachu", "numero": 25, "tipo": ["Eléctrico"]},
    {"nombre": "Charizard", "numero": 6, "tipo": ["Fuego", "Volador"]},
    {"nombre": "Jolteon", "numero": 135, "tipo": ["Electrico"]},
    {"nombre": "Lycanroc", "numero": 745, "tipo": ["Roca"]},
    {"nombre": "Tyrantrum", "numero": 697, "tipo": ["Roca", "Dragon"]},
    
]

nombre_tree = BinaryTree()
numero_tree = BinaryTree()
tipo_tree = BinaryTree()

#A
for pokemon in pokemon_list:
    nombre_tree.insert_node(pokemon['nombre'], {'numero': pokemon['numero'],'tipo': pokemon['tipo']})
    numero_tree.insert_node(pokemon['nombre'], {'numero': pokemon['numero'],'tipo': pokemon['tipo']})
    tipo_tree.insert_node(pokemon['nombre'], {'numero': pokemon['numero'],'tipo': pokemon['tipo']})

#B
num = 25
numero_tree.inorden(num)
nombre = 'Bul'
nombre_tree.search_by_coincidence(nombre)
tipo = 'Electrico'
tipo_tree.inorden(tipo)

#C
def listar_nombres_por_tipo(self, root, tipo):
    if root is not None:
        if tipo in root.value['tipo']:
            print(root.value['nombre'])
        self.listar_nombres_por_tipo(root.left, tipo)
        self.listar_nombres_por_tipo(root.right, tipo)

filtrar_por = ['Agua','Fuego', 'Planta','Electrico']
print('Nombres de Pokémon de tipo Agua:')
tipo_tree.listar_nombres_por_tipo(tipo_tree.root, filtrar_por)

#D
print('Listado de Pokémon en orden ascendente por número:')
numero_tree.inorden()
print('\nListado de Pokémon en orden ascendente por nombre:')
nombre_tree.inorden()
print('Listado de Pokémon por nivel nombre')
nombre_tree.by_level()

#E
print('Datos de Pokémon Jolteon:')
nombre_tree.search_pokemon_by_nombre('Jolteon')
print('\nDatos de Pokémon Lycanroc:')
nombre_tree.search_pokemon_by_nombre('Lycanroc')
print('\nDatos de Pokémon Tyrantrum:')
nombre_tree.search_pokemon_by_nombre('Tyrantrum')

#F
print(f"Total de Pokémon de tipo 'Eléctrico' : { tipo_tree.contar ('Eléctrico') }")
print(f"Total de Pokémon de tipo 'Acero': { tipo_tree.contar ('Acero') }")