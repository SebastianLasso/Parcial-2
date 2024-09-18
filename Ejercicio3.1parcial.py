# Tomar una cadena de texto del usuario 
texto = input("Ingrese una cadena de texto: ")

# Convertir a Mayusculas
texto_mayus = texto.upper()

# Contar caracteres
longitud  = len(texto)

#Verificar si contiene la palabra "python"

contiene_python = "python" in texto

#Mostrar los resultados
print(f"Texto en mayusculas: {texto_mayus}")
print(f"Numero de caracteres: {longitud}")
print(f"Contiene la palabra: {contiene_python}")