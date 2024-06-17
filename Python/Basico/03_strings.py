### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

# Formateo

name, surname, age = "Renzo", "Barreto", 25
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age)) # %s formato cadena, %d formato tipo numero
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age)) # Esta forma no es recomendado
print(f"Mi nombre es {name} {surname} y mi edad es {age}") # forma resumida de mostrar el formato de dato visualizar

# Desempaqueado de caracteres

language = "python"
a, b, c, d, e, f = language # p, y, t, h, o, n
print(a) # p
print(e) # o

# División

language_slice = language[1:3]
print(language_slice) # yt

language_slice = language[1:]
print(language_slice) # ython

language_slice = language[-2]
print(language_slice) # o

language_slice = language[0:6:2]
print(language_slice) # pto, avanza de 2 en 2 en el rango dado

# Reverse

reversed_language = language[::-1]
print(reversed_language) #nohtyp

# Funciones del lenguaje

print(language.capitalize()) # Python
print(language.upper()) # PYTHON # el texto en mayuscula
print(language.count("t")) # 1 # numero de veces que aparece la letra t
print(language.isnumeric()) # False # confirma si el valor de la variable es un numero
print("1".isnumeric()) # True #confirma si 1 es un numero
print(language.lower()) # python # el texto en minuscula
print(language.lower().isupper()) # convierte el texto en minuscula yu verifica si hay alguna mayuscula
print(language.startswith("Py")) # el texto empieza por Py
print("Py" == "py")  # No es lo mismo