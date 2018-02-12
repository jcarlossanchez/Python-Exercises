input_user = input("Ingrese un numero entero: ")
numero_entero = int(input_user)
divisible_tres = numero_entero % 3
if divisible_tres == 0:
    print('Yes')
else:
    print('No')
