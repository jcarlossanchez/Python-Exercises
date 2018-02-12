input_user = input('Escribe un numero entero: ')
entero = int(input_user)
if entero % 2 == 0 and entero % 3 == 0:
    print('BOTH')
elif entero % 2 == 0 or entero % 3 == 0:
    print('ONE')
elif entero% 2 != 0 and entero % 3 != 0:
    print('NEITHER')
