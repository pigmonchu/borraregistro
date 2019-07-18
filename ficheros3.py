from os import remove, rename
FORIGINAL = 'movimientos.txt'
FCOPIA = 'nmovimientos.txt'

fe = open(FORIGINAL, 'r')
fs = open(FCOPIA, 'w')

ix = int(input("Registro: "))

contador = 1
linea = fe.readline()
while linea != '':
    if contador != ix:
        fs.write(linea)
    contador += 1
    linea = fe.readline()

fe.close()
fs.close()

remove(FORIGINAL)
rename(FCOPIA, FORIGINAL)