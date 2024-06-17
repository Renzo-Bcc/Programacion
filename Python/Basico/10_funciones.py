### Functions ###

# Definición

def my_function():
    print("Esto es una función")


my_function() # Esto es una función
my_function() # Esto es una función
my_function() # Esto es una función

# Función con parámetros de entrada/argumentos


def sum_two_values(first_value: int, second_value):
    print(first_value + second_value)


sum_two_values(5, 7) # 12
sum_two_values(54754, 71231) # 125985
sum_two_values("5", "7") # 57
sum_two_values(1.4, 5.2) # 6.6

# Función con parámetros de entrada/argumentos y retorno


def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum # none


my_result = sum_two_values(1.4, 5.2)
print(my_result) # 6.6

my_result = sum_two_values_with_return(10, 5)
print(my_result) # 15

# Función con parámetros de entrada/argumentos por clave


def print_name(name, surname):
    print(f"{name} {surname}")


print_name(surname="Moure", name="Brais") # Brais Moure

# Función con parámetros de entrada/argumentos por defecto


def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")


print_name_with_default("Brais", "Moure") # Brais Moure Sin alias
print_name_with_default("Brais", "Moure", "MoureDev") # Brais Moure MoureDev

# Función con parámetros de entrada/argumentos arbitrarios


def print_upper_texts(*texts):
    print(type(texts)) # <class 'tuple'>
    for text in texts:
        print(text.upper())


print_upper_texts("Hola", "Python", "MoureDev") # HOLA, PYTHON, MOUREDEV
print_upper_texts("Hola") # HOLA