### Listas ###

# Definición

my_list = list()
my_other_list = []

print(len(my_list)) # Longitud de la lista, 0

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list) # [35, 24, 62, 52, 30, 30, 17]
print(len(my_list)) # 7

my_other_list = [25, 1.65, "Renzo", "Barreto"]

print(type(my_list)) # <class 'list'>
print(type(my_other_list)) # <class 'list'>

# Acceso a elementos y búsqueda

print(my_other_list[0]) # 25
print(my_other_list[1]) # 1.65
print(my_other_list[2]) # Renzo
print(my_other_list[3]) # Barreto
print(my_other_list[-1]) # Barreto
print(my_other_list[-4]) # 25
print(my_list.count(30)) # 2, Cuenta elementos dentro de la misma lista
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError

print(my_other_list.index("Renzo")) # 2

age, height, name, surname = my_other_list
print(name) # Renzo

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age) # 25

# Concatenación

print(my_list + my_other_list) # [35, 24, 62, 52, 30, 30, 17, 25, 1.65, 'Renzo', 'Barreto']
#print(my_list - my_other_list)

# Creación, inserción, actualización y eliminación

my_other_list.append("Python")
print(my_other_list) # [25, 1.65, 'Renzo', 'Barreto', 'Python']

my_other_list.insert(1, "Rojo")
print(my_other_list) # [25, 'Rojo', 1.65, 'Renzo', 'Barreto', 'Python']

my_other_list[1] = "Azul"
print(my_other_list) # [25, 'Azul', 1.65, 'Renzo', 'Barreto', 'Python']

my_other_list.remove("Azul")
print(my_other_list) # [25, 1.65, 'Renzo', 'Barreto', 'Python']

my_list.remove(30) # Elimina el valor encontrado
print(my_list) # [35, 24, 62, 52, 30, 17]

print(my_list.pop()) # 17, Elimina el ultimo elemento de la lista
print(my_list) # [35, 24, 62, 52, 30]

my_pop_element = my_list.pop(2) # 62, Elimina el elemento con indice 2 pero lo guardas en otra variable
print(my_pop_element) # 62, Muestra el elemento eliminado
print(my_list) # [35, 24, 52, 30], Muestra la lista con el indice eliminado

del my_list[2] # 52, Borra el elemento de indice 2
print(my_list) # [35, 24, 30]

# Operaciones con listas

my_new_list = my_list.copy()

my_list.clear() # Borra los elementos de la lista
print(my_list) # []
print(my_new_list) # [35, 24, 30]

my_new_list.reverse() # Intercambia el orden de los elementos de la lista
print(my_new_list) # [30, 24, 35]

my_new_list.sort() # Ordena los elementos de la lista
print(my_new_list) # [24, 30, 35]

# Sublistas

print(my_new_list[1:3]) # [30, 35]

# Cambio de tipo

my_list = "Hola Python"
print(my_list) # Hola Python
print(type(my_list)) # <class 'str'>