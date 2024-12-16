#Programacion tradicional

def ingresar_temperaturas():
    # Lista para almacenar las temperaturas de cada día
    temperaturas = []
    # Iteramos sobre los días de la semana (1 al 7)
    for dia in range(1, 8):
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal de temperaturas
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Menú o mensaje de inicio
print("*** Programación Tradicional ***")

# Llamamos a la función para ingresar temperaturas
temperaturas = ingresar_temperaturas()

# Calculamos el promedio de las temperaturas
promedio = calcular_promedio(temperaturas)

# Mostramos el promedio con dos decimales
print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")
