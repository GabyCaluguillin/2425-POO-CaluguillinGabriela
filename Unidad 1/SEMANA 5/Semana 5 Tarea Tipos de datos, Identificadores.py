# Programa para calcular el área de diferentes figuras geométricas utilizando POO
# Funcionalidades: calcular el área de un círculo, cuadrado o rectángulo

import math

# Clase base para figuras geométricas
class FiguraGeometrica:
    def calcular_area(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

# Clase para el círculo
class Circulo(FiguraGeometrica):
    def __init__(self, radio: float):
        self.radio = radio

    def calcular_area(self) -> float:
        """Calcula el área del círculo."""
        return math.pi * self.radio ** 2

# Clase para el cuadrado
class Cuadrado(FiguraGeometrica):
    def __init__(self, lado: float):
        self.lado = lado

    def calcular_area(self) -> float:
        """Calcula el área del cuadrado."""
        return self.lado ** 2

# Clase para el rectángulo
class Rectangulo(FiguraGeometrica):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        """Calcula el área del rectángulo."""
        return self.base * self.altura

def main():
    print("Bienvenido al calculador de áreas.")

    # Solicitar al usuario qué figura desea calcular
    figura = input("¿De qué figura deseas calcular el área? (círculo/cuadrado/rectángulo): ").strip().lower()

    if figura == "círculo":
        radio = float(input("Introduce el radio del círculo: "))
        circulo = Circulo(radio)
        area = circulo.calcular_area()
        print(f"El área del círculo es: {area:.2f}")

    elif figura == "cuadrado":
        lado = float(input("Introduce el lado del cuadrado: "))
        cuadrado = Cuadrado(lado)
        area = cuadrado.calcular_area()
        print(f"El área del cuadrado es: {area:.2f}")

    elif figura == "rectángulo":
        base = float(input("Introduce la base del rectángulo: "))
        altura = float(input("Introduce la altura del rectángulo: "))
        rectangulo = Rectangulo(base, altura)
        area = rectangulo.calcular_area()
        print(f"El área del rectángulo es: {area:.2f}")

    else:
        print("Figura no reconocida. Por favor, introduce círculo, cuadrado o rectángulo.")

if __name__ == "__main__":
    main()
