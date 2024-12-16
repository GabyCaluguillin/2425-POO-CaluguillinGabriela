# Programación Orientada a Objetos (POO)

class ClimaSemanal:
    # Clase que representa la información de clima semanal
    def __init__(self):
        self.temperaturas = []  # Lista para almacenar las temperaturas de los 7 días

    def ingresar_temperaturas(self):
        # Permite ingresar las temperaturas diarias
        for dia in range(1, 8):
            temp = float(input(f"Ingresa la temperatura díaria {dia}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        # Calcula el promedio semanal de temperaturas
        return sum(self.temperaturas) / len(self.temperaturas)

#Flujo del POO
print("\n--Programacion Orientada a Objetos--")
clima = ClimaSemanal()
clima.ingresar_temperaturas()
promedio_POO = clima.calcular_promedio()
print(f"Promedio semanal de temperaturas : {promedio_POO:.2f} °C")