### Tuples ###

# Definición
# Tupla: es un conjunto de valores, luego de definirlas no se pueden modificar ('inmutables')

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Renzo", "Barreto", "Renzo")
my_other_tuple = (35, 60, 30)

print(my_tuple) # (35, 1.77, 'Renzo', 'Barreto', 'Renzo')
print(type(my_tuple)) # <class 'tuple'>

# Acceso a elementos y búsqueda

print(my_tuple[0]) # 35
print(my_tuple[-1]) # Renzo
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

print(my_tuple.count("Renzo")) # Cuantas veces el tuple tiene ese elemento, 2
print(my_tuple.index("Barreto")) # En que posicion se encuentra dicho elemento, 3
print(my_tuple.index("Renzo")) # 2

# my_tuple[1] = 1.80 'tuple' object does not support item assignment # tupla es inmutable

# Concatenación

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple) # (35, 1.77, 'Renzo', 'Barreto', 'Renzo', 35, 60, 30)

# Subtuplas

print(my_sum_tuple[3:6]) # La tupla comienza con el indice y termina antes del segundo indice # ('Barreto', 'Renzo', 35)

# Tupla mutable con conversión a lista

my_tuple = list(my_tuple)
print(my_tuple) # [35, 1.77, 'Renzo', 'Barreto', 'Renzo']
print(type(my_tuple)) # <class 'list'>

my_tuple[4] = "Ingeniero de Sistemas"
my_tuple.insert(1, "Azul")

my_tuple = tuple(my_tuple)
print(my_tuple) # (35, 'Azul', 1.77, 'Renzo', 'Barreto', 'Ingeniero de Sistemas')
print(type(my_tuple)) # <class 'tuple'>

# Eliminación

# del my_tuple[2] TipoDeError: 'tuple' El objeto no admite la eliminacion de elementos

del my_tuple
# print(my_tuple) ErrorDeNombre: name 'my_tuple' no esta definido