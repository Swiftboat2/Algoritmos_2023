class BitacoraNave:
    def __init__(self):
        self.pila = []

    def ag_mision(self, planeta, capturado, recompensa):
        self.pila.append((planeta, capturado, recompensa))

    def mostrar_planetas_visitados(self):
        planetas_visitados = [mision[0] for mision in self.pila]
        return planetas_visitados

    def calcular_recaudacion_total(self):
        recaudacion_total = sum(mision[2] for mision in self.pila)
        return recaudacion_total

    def buscar_mision_han_solo(self):
        for i, mision in enumerate(self.pila):
            if mision[1] == "Han Solo":
                return i+1, mision[0]
        return None, None
    
bitacora = BitacoraNave()

bitacora.ag_mision("Abafar", "Han Solo", 5004000)
bitacora.ag_mision("Chandrila", "Snoke", 150000)
bitacora.ag_mision("Dorin", "Xizor", 120000)
bitacora.ag_mision("Er'Kit", "Sev’rance Tann", 900000)

planetas = bitacora.mostrar_planetas_visitados()
print("Planetas visitados:", planetas)

recaudacion_total = bitacora.calcular_recaudacion_total()
print("Recaudación total:", recaudacion_total)

num_mision, planeta = bitacora.buscar_mision_han_solo()
if num_mision is not None:
    print("Capturó a Han Solo en la misión", num_mision, "en el planeta", planeta)
else:
    print("No se encontró información sobre la captura de Han Solo.")
