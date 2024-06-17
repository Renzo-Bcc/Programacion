### Operadores Aritméticos ###

# Operacines con enteros
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 2)
print(10 // 3) # Una division aproximada a su numero entero
print(2 ** 3 + 3 - 7 / 1 // 4)

# Operaciones con cadenas de texto
print("hola " + "python " + "¿Que tal?")
print("hola " + str(5))

# Operaciones mixtas
print("hola " * 5)
print("hola " * (2 ** 3))

my_float = 2.5 * 2
print("hola" * int(my_float))

### Operadores Comparativos ###

# Operaciones con enteros
print(3 > 4)  # False
print(3 < 4)  # True
print(3 >= 4) # False
print(4 <= 4) # True
print(3 == 4) # False
print(3 != 4) # True

# Operaciones con cadenas de texto
print("Hola" > "Python")  # False
print("Hola" < "Python")  # True
print("aaaa" >= "abaa")   # False # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa")) # True # Cuenta caracteres
print("Hola" <= "Python") # True
print("Hola" == "Hola")   # True
print("Hola" != "Python") # True

### Operadores Lógicos ###

# Basada en el Álgebra de Boole
print(3 > 4 and "Hola" > "Python") # False
print(3 > 4 or  "Hola" > "Python") # False
print(3 < 4 and "Hola" < "Python") # True
print(3 < 4 or  "Hola" > "Python") # True
print(3 < 4 or ("Hola" > "Python" and 4 == 4)) # True
print(not (3 > 4)) # True