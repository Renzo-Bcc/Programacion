### Dictionaries ###

# Definición
# Es un tipo de estructura donde guardamos un tipo de dato de identidad - valor

my_dict = dict()
my_other_dict = {}

print(type(my_dict)) # <class 'dict'>
print(type(my_other_dict)) # <class 'dict'>

my_other_dict = {"Nombre": "Renzo", "Apellido": "Barreto", "Edad": 25, 1: "Python"}

my_dict = {
    "Nombre": "Maria",
    "Apellido": "Balarezo",
    "Edad": 35,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.77
}

print(my_other_dict) # {"Nombre": "Renzo", "Apellido": "Barreto", "Edad": 25, 1: "Python"}
print(my_dict) # {"Nombre": "Maria", "Apellido": "Balarezo", "Edad": 35, Lenguajes: {"Python", "Swift", "Kotlin"}, 1: 1.77}

print(len(my_other_dict)) # 4
print(len(my_dict)) # 5

# Búsqueda

print(my_dict[1]) # Apellido
print(my_dict["Nombre"]) # Maria

print("Moure" in my_dict) # False
print("Apellido" in my_dict) # True

# Inserción

my_dict["Calle"] = "Calle MoureDev"
print(my_dict) # {"Nombre": "Maria", "Apellido": "Balarezo", "Edad": 35, Lenguajes: {"Python", "Swift", "Kotlin"}, 1: 1.77, "Calle": "Calle Mouredev"}

# Actualización

my_dict["Nombre"] = "Paula"
print(my_dict["Nombre"]) # Paula

# Eliminación

del my_dict["Calle"]
print(my_dict) # {"Nombre": "Paula", "Apellido": "Balarezo", "Edad": 35, Lenguajes: {"Python", "Swift", "Kotlin"}, 1: 1.77}

# Otras operaciones

print(my_dict.items()) # dict_items([('Nombre', 'Paula'), ('Apellido', 'Balarezo'), ('Edad', 35), ('Lenguajes', {'Swift', 'Kotlin', 'Python'}), (1, 1.77)])
print(my_dict.keys()) # dict_keys(['Nombre', 'Apellido', 'Edad', 'Lenguajes', 1])
print(my_dict.values()) # dict_values(['Paula', 'Balarezo', 35, {'Swift', 'Kotlin', 'Python'}, 1.77])

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict) # {'Nombre': None, 1: None, 'Piso': None}
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict)) # {'Nombre': None, 1: None, 'Piso': None}
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict)) # {'Nombre': None, 'Apellido': None, 'Edad': None, 'Lenguajes': None, 1: None}
my_new_dict = dict.fromkeys(my_dict, "MoureDev")
print((my_new_dict)) # {'Nombre': 'MoureDev', 'Apellido': 'MoureDev', 'Edad': 'MoureDev', 'Lenguajes': 'MoureDev', 1: 'MoureDev'}

my_values = my_new_dict.values()
print(type(my_values)) # <class 'dict_values'>

print(my_new_dict.values()) # dict_values(['MoureDev', 'MoureDev', 'MoureDev', 'MoureDev', 'MoureDev'])
print(list(dict.fromkeys(list(my_new_dict.values())).keys())) # ['MoureDev']
print(tuple(my_new_dict)) # ('Nombre', 'Apellido', 'Edad', 'Lenguajes', 1)
print(set(my_new_dict)) # {1, 'Nombre', 'Apellido', 'Lenguajes', 'Edad'}