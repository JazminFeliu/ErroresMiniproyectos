import reflex as rx

def numeroALetra(num):
    '''
    Convertimos un numero entero de hasta tres dígitos a su representación en letras.
    Ejemplo: 987: Novescientos ochenta y siete
    Lo vamos a mostrar con una webapp realizada en python, con el framework Reflex.
    '''

    if num == 0:
        return'Cero'
    
    numALetra = ''
    unidades = ['','uno','dos', 'tres', 'cuatro','cinco', 'seis', 'siete', 'ocho', 'nueve']
    decenas = ['', 'dieci', 'veinti', 'treinta y ', 'cuarenta y ', 'cincuenta y ','sesenta y ', 'setenta y ', 'ochenta y ', 'noventa y ']
    centenas = ['', 'ciento', 'doscientos', 'trescientos', 'cuatroscientos', 'quinientos', 'seiscientos', 'setecientos', 'ochocientos', 'novecientos']
    num = '0' * (3-len(str(num)))+ str(num)

    unidad = int(num[-1])
    decena = int(num[-2])
    centena = int(num[-3])

    numALetra = '{} {}{}'.format(centenas[centena], decenas[decena], unidades[unidad]).strip()

    numALetra = numALetra.replace('dieciuno', 'once')
    numALetra = numALetra.replace('diecidos', 'doce')
    numALetra = numALetra.replace('diecitres', 'trece')
    numALetra = numALetra.replace('diecicuatro', 'catorce')
    numALetra = numALetra.replace('diecicinco', 'quince')  

    if numALetra.endswith('dieci'):
        numALetra = numALetra.replace('dieci', 'diez')
    elif numALetra.endswith('veinti'):
        numALetra = numALetra.replace('veinti', 'veinte') 
    elif numALetra.endswith(' y'):
        numALetra = numALetra[:-2]
    elif numALetra.endswith('ciento'):
        numALetra = numALetra.replace('ciento', 'cien')            

    return numALetra.capitalize()

valor = 793

print(numeroALetra(valor))