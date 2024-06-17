### Variables ###

my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable =str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenacion de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola linea ¡Cuidao con abusar de esta sintaxis!
name, surname, alias, edad = "Renzo", "Barreto", "Chavo", 25
print("Me llamo:", name, surname, "Mi edad es:", edad, "Y mi alias es:", alias)

# Inputs
first_name =input('¿Cual es tu nombre? ')
age = input('¿Cuantos años tienes? ')
print(first_name)
print(age)

# Cambiamos su tipo
name = 123
age = "Renzo"
print(name)
print(age)

# ¿Forzamos el tipo de dato?
address: str = "Mi dirección"
address = False
address = 9
address = 32.3
print(type(address))