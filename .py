def main():
    """procesador de textos experimental, python 2.7, estructura de diccionarios y listas """
    string = input ("Seleccione la opcion que desea ejecutar: ")
    print ""
    print "Opcion 1: Cuenta caracteres de un string"
    print "Opcion 2: Cuenta la cantidad de apariciones de una letra o caracter en un string"
    print "Opcion 3: Cuenta la cantidad de apariciones de una palabra en un string"
    print "Opcion 4: Cuenta la cantidad de palabras de un string"
    print ""
    print "ingrese * para salir."
    print "============================="
    
def cuenta_caracteres(string):
    dicc = {}
    for x in string:
        if x == "" or " ":
            pass
        elif x not in dicc.keys():
            dicc[x] = 1
        elif x in dicc.keys():
            dicc[x] = dicc[x] + 1
    return dicc

