tempo_segundos = int(input())

horas = tempo_segundos//3600
minutos = (tempo_segundos%3600) //60
segundos = (tempo_segundos%3600) % 60



print(f"{horas:.0f}:{minutos:.0f}:{segundos:.0f}")