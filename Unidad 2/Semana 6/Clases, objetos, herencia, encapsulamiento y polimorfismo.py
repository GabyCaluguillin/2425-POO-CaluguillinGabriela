# Clase base

class vehiculo:
    def __init__(self, marca, modelo):
        self.__marca = marca  #Atributo privado
        self.__modelo = modelo  #Atributo privado

#Métodos getter para acceder a los atributos privados
    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

#Métodos que serán sobreescritos en la clase derrivada

    def arrancar(self):
        return "El vehiculo va a arrancar"
    def caminar(self):
        return "El vehiculo esta caminando"
#Clase derivada
class carro(vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo) #Llamada al constructor de la clase base
        self.puertas = puertas #Atributo público

#Sobreescritura de los métodos arrancar y caminar (polimorfismo)
    def arrancar(self):
        return f"El carro {self.get_marca()} {self.get_modelo()} está arrancando"
    def caminar(self):
        return f"El carro {self.get_marca()} {self.get_modelo()} está caminando"

# Creación de la instancia de la clase carro
mi_carro = carro("Renault", "Logan", 4)

# Uso de los métodos utilizados

print(f"marca: {mi_carro.get_marca()}")
print(f"modelo: {mi_carro.get_modelo()}")
print(f"número de puertas: {mi_carro.puertas}")
print(mi_carro.arrancar())
print(mi_carro.caminar())
