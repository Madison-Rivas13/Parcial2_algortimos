#plantear una funcion que reciba un string en mayusculas o minusculas y una letra, luego el programa debe indicarle cuantas veces se encuentra la letra dentro del string ingresado 

def contar_letra(string, letra):
    string = string.lower()
    letra = letra.lower()
    cantidad = string.count(letra)
    
    return cantidad

cadena = "Ejemplo de una cadena de texto para buscar la letra e"
letra_buscar = "e"
resultado = contar_letra(cadena, letra_buscar,)

print(f'La letra "{letra_buscar}" aparece {resultado} veces en la cadena.')
