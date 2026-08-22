age = int(input("Cuantos años tiene: "))

if age < 0:
    print("Metalo bien ñero")
elif age <= 8:
    print("Eres un bebe")
elif age <= 12:
    print("Eres un niño")
elif age <= 18:
    print("Eres un joven")
else:
    print("Eres un viejo")

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
print("1. suma")
print("2. resta")
print("3. multiplicacion")
print("4. dividir")

oper = int(input("Ingrese la operacion a realizar: "))

match oper:
    case 1:
        print(num1 + num2)

    case 2:
        print(num1 - num2)

    case 3:
        print(num1 * num2)

    case 4:
        print(num1 / num2)

    case _:
        print("Operacion invalido")
