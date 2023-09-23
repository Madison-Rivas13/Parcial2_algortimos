mail = input("Ingrese un mail: ")
cantidad = 0  
x = 0  


while x < len(mail):
    if mail[x] == "@":
        cantidad += 1  
    x += 1  

if cantidad == 1:
    print("contiene solo un símbolo '@' el mail ingresado.")
elif cantidad > 1:
    print("El correo electrónico ingresado contiene más de un símbolo '@'.")
else:
    print("Incorrecto.")
