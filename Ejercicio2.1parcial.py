# Pedir la temperatura en grados fahrenheit

fahrenheit= float(input("Ingrese la temperatura en fahrenheit: "))

# Convertir a grados celsius 

celsius= (5 / 9) * (fahrenheit - 32 )

# Convertir a grados Kelvin

kelvin= (5 / 9) * (fahrenheit - 32) + 273.15

# Mostrar el resultado

print(f"Temperatura en grados Celsius: {celsius: .2f} ")
print(f"Temperatura en grados Kelvin: {kelvin: .2f} ")
