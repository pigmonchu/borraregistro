from os import remove, rename
FORIGINAL = 'movimientos.txt'
FCOPIA = 'nmovimientos.txt'

fe = open(FORIGINAL, 'r')
fs = open(FCOPIA, 'w')

ix = int(input("Registro: "))

contador = 1
for linea in fe:
    if contador != ix:
        fs.write(linea)
    contador += 1
fe.close()
fs.close()

remove(FORIGINAL)
rename(FCOPIA, FORIGINAL)