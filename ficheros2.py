from os import remove
from os import rename

ficheroentrada = open('movimientos.txt', 'r')
ficherosalida = open('nuevomovimientos.txt', 'w')

ix = input("Registro a borrar")
ix = int(ix)

lineas= ficheroentrada.readlines()
nLineas = len(lineas)
LL = 1

if ix <= nLineas and ix > 0:
    '''
    for linea in lineas:
        if ix != LL:
            ficherosalida.write(linea)
        LL += 1 
    '''

    for num_linea in range (0, nLineas):
        if ix != num_linea+1:
            nuevalinea = lineas[num_linea]
            ficherosalida.write(nuevalinea)

else:
    num_linea = 0
    print('valor introducido no válido')

ficherosalida.close()
ficheroentrada.close()

if num_linea:
    remove("movimientos.txt")
    rename('nuevomovimientos.txt','movimientos.txt')
else:
    remove('nuevomovimientos.txt')
