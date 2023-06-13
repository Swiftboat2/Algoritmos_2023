def contador_palabra(array, palabra):
    if not array: 
        return 0
    elif array[0] == palabra: 
        return 1 + contador_palabra(array[1:], palabra)  
    else:
        return contador_palabra(array[1:], palabra) 
array_palabras = ["algoritmo", "sistemas", "algoritmo", "parcial", "algoritmo"]
palabra_buscada = "algoritmo"
contador = contador_palabra(array_palabras, palabra_buscada)
print(f"La palabra '{palabra_buscada}' aparece {contador} veces en el vector.")