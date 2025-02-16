m = int(input("Encontrar el número mayor, ingresa 1 para entrar al sistema"))
if m == 1:
    print ("Los números a ingresar deben ser extrictamente diferentes")
    x = float(input("Ingresa el primer número"))
    y = float(input("Ingresa el segundo número"))
    z = float(input("Ingresa el tercer número"))
    if x == y or x==z or y==z:
      print("Extrictamente iguales dije >:c")
      m = int(input("Deseas seguir con las reglas ahora sí bien? Ingresa 1 si sí"))
    if m == 1:
     print ("Los números a ingresar deben ser extrictamente diferentes")
     x = float(input("Ingresa el primer número"))
     y = float(input("Ingresa el segundo número"))
     z = float(input("Ingresa el tercer número"))
    if x > y and x > z:
     print (x, "Es el número mayor")
    elif y > x and y > z:
     print (y, "es el número mayor")
    else:
     print (z, "es el número mayor")
else:
 print ("Bueno, es todo bai")   
