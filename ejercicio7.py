print("Determinar si un número es par o impar")
n = float(input("¿Quieres determinar si un número es par o impar? Presiona 1 si es así"))
if n > 1 :
    print("Ah... Supongo que no querías, buenoo")
elif n < 1 :
 print("Ah... Supongo que no querías, buenoo")
elif n:
 x = float(input("Bien! Dame un número para comenzar"))
pip = x % 2
if pip == 0 :
  print(x, "Es par")
else:
  print(x, "Es impar")
  