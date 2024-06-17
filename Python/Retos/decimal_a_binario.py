'''
Decimal a Binario
crea una funcion que se encargue de
transformar un numero decimal a binario
'''
def decimal_a_binario(decimal):
    binario = ""
    while decimal > 0:
        binario = f"{decimal % 2}{binario}"
        decimal //= 2
    return 0 if binario == "" else  binario

print(decimal_a_binario(10)) # imprime 1010
print(decimal_a_binario(387)) # imprime 110000011