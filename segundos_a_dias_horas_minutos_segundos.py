input_user = input('Escribe el numero de segundos: ')
segundos = int(input_user)
dias = (segundos // 86400)
horas = (segundos - (dias * 86400) ) // 3600
minutos = ( segundos - (dias * 86400) - (horas * 3600) ) // 60
segundos = segundos % 60
print(dias,'days',horas,'hours',minutos,'minutes',segundos,'seconds')
