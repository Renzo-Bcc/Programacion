'''
Contador de vocales
Crea un programa que cuente cuantas 
vocales tiene una cadena de texto
'''
vocales = "aeiou"
counter = 0
cadena = str(input("Introduce una cadena de texto: "))
for char in cadena.lower():
    if char in vocales:
        counter +=1

print(f"La cadena tiene {counter} vocales")