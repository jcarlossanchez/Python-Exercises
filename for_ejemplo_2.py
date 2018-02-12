input_user = input('Escribe un numero entero: ')
entero = int(input_user) + 1
total = 0
for x in range(1, entero):
    total = total + x
print(total)
