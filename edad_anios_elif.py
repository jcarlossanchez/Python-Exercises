input_user = input ('Escriba su edad en años: ')
anios = int(input_user)
if anios <= 0:
    print('UNBORN')
elif anios >0 and anios <= 150:
    print('ALIVE')
elif anios >150:
    print('VAMPIRE')
