class Persona:
    def __init__(self, nombre,edad):
        self.__nombre = nombre
        self.__edad = edad

#Getter para el nombre
def get_nombre(self):
    return self.__nombre

#Setter para el nombre
def set_nombre(self, nombre):
    self.__nombre = nombre

#Getter para la edad
def get_edad(self):
    return self.__edad

#Setter para la edad, controlando que no sea negativo
def set_edad(self, edad):
    if edad >=0:
        self.__edad = edad
    else:
        print("La edad no puede ser negativa.")

#Uso de la clase persona
persona = Persona("Carlos", 28)

# Intentando acceder a los atributos privados (esta causara error)
#print(persona.__nombre)  # No se puede acceder directamente

#Acceder a traves de los metodos publicos 
print(persona.get_nombre()) # Carlos
print(persona.get_edad()) # 28

#Cambiar el valor usando setters
persona.set_nombre("Juan")
persona.set_edad(30)

#Intentar establecer una edad negativa
persona.set_edad(-5)

#Verificar cambios 
print(persona.get_nombre()) # Juan
print(persona.get_edad()) # 30