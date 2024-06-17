'''
Par o Impar
Crea una funcion que comprueve 
si un numero es par o impar
'''
'''
# Mi forma
def par_o_impar(numero):
    if numero % 2 == 0:
        return "El número es par"
    else:
        return "El número es impar"

numero = int(input("Introduce un número entero: "))
print("El número seleccionado es: " + str(numero))
numero = par_o_impar(numero)
print(numero)
'''
# Mouredev
try:
    num = int(input("Introduce un número entero: "))
    if num % 2 == 0:
        print(f"El numero {num} es par")
    else:
        print(f"El número {num} es impar")
except ValueError:
    print("La entrad no es valida")