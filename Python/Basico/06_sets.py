### Sets ###

# Definición: 
# Un set no es una estructura ordenada
# Un set no admite repetidos

my_set = set()
my_other_set = {} # inicia siendo 'dict'

print(type(my_set)) # <class 'set'>
print(type(my_other_set))  # <class 'dict'> Inicialmente es un diccionario 

my_other_set = {"Renzo", "Barreto", 25}
print(type(my_other_set)) # <class 'set'> Ahora es Set

print(len(my_other_set)) # 3 elementos

# Inserción

my_other_set.add("Ingeniero de Sistemas")

print(my_other_set)  # {'Ingeniero de Sistemas', 'Renzo', 'Barreto', 25}

my_other_set.add("MoureDev")

print(my_other_set) # {'MoureDev', 'Renzo', 'Barreto', 'Ingeniero de Sistemas', 25}

# Búsqueda

print("Barreto" in my_other_set) # True
print("Renzo" in my_other_set) # True
print("Sistemas" in my_other_set) # False

# Eliminación

my_other_set.remove("MoureDev")
print(my_other_set) # {'Renzo', 'Barreto', 'Ingeniero de Sistemas', 25}

my_other_set.clear()
print(len(my_other_set)) # 0

my_other_set = {"Paula", "Martínez", "Balarezo", 26}
print(my_other_set) # {'Balarezo', 26, 'Paula', 'Martínez'}

del my_other_set
# print(my_other_set) ErrorDeNombre: name 'my_other_set' sucede cuando el Set no esta definido
# Para evitar el error defini el Set para

# Transformación

my_set = {"María", "Teresa","Martínez", 50}
my_list = list(my_set)
print(my_list) # [50, 'Martínez', 'María', 'Teresa']
print(my_list[0]) # 50

my_other_set = {"Kotlin", "Swift", "Python"}
print(my_other_set) # {'Python', 'Swift', 'Kotlin'}

# Otras operaciones

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"})) # {'C#', 'María', 'Python', 'Kotlin', 'JavaScript', 50, 'Martínez', 'Swift', 'Teresa'}
print(my_new_set.difference(my_set)) # {'Python', 'Swift', 'Kotlin'}