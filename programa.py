from datetime import datetime

t = str(datetime.now())
texto = "Este programa foi executado em %s" %t

file = open('data2.txt', 'w')
file.write(texto)
file.close()
