#Desarrollar un programa que por linea de comandos debe recibir "N" cantidad de valores separados por comas y el programa debe devolver la suma y el promedio de todo el conjunto, tanto la suma como el promedio debe estar escritos por funciones ejemplo de ejecucion 

def contar_letra_en_string(cadena, letra):
 
    cadena = cadena.lower()
    letra = letra.lower()
    
    contador = cadena.count(letra)
    return contador

def calcular_suma_promedio(valores):

    valores = [float(valor) for valor in valores]
    
    suma = sum(valores)
    promedio = suma / len(valores)
    
    return suma, promedio

if __name__ == "_main_":
    cadena_palabra_a_leer = "Computadora"
    letra_a_buscar = "o"
    resultado = contar_letra_en_string(cadena_palabra_a_leer, letra_a_buscar)
    print(f"La letra '{letra_a_buscar}' aparece {resultado} veces en la cadena '{cadena_palabra_a_leer}'.")
    
    valores_ejemplo = input("Ingrese los valores separados por comas: ").split(',')
    suma_ejemp, promedio_ejemp = calcular_suma_promedio(valores_ejemplo)
    print(f"La suma de los valores es: {suma_ejemp}")
    print(f"El promedio de los valores es: {promedio_ejemp}")

