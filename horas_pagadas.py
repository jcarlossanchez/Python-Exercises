input_user = input('Ingrese las horas trabajadas: ')
horas = int(input_user)
if horas < 0 or horas > 168:
    print('INVALID')
else:
    if horas >= 0 and horas < 41:
        total = horas * 8
        print('YOU MADE',total,'DOLLARS THIS WEEK')
    elif horas > 40 and horas <= 50:
        horas_extra = (horas - 40) * 9
        total = (40 * 8) + horas_extra
        print('YOU MADE',total,'DOLLARS THIS WEEK')
    elif horas > 50:
        horas_extra = (horas - 50) * 10
        total = ( (40 * 8) + (10 * 9) ) + horas_extra
        print('YOU MADE',total,'DOLLARS THIS WEEK')
