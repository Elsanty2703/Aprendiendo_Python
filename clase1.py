name = "Santy"
print(f"Hola {name}")

print("Primer ejercicio: Condicionales")

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

print("Segundo ejercicio: Match")

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
print("1. suma")
print("2. resta")
print("3. multiplicacion")
print("4. dividir")

oper = int(input("Ingrese la operacion a realizar: "))

match oper:
    case 1:
        print(f"La suma da: {num1 + num2}")

    case 2:
        print(f"La resta da: {num1 - num2}")

    case 3:
        print(f"La multiplicacion da: {num1 * num2}")

    case 4:
        if num2 == 0:
            while(num2 == 0):
                print("no se puede bobo")
                num2 = int(input("Ingrese otro numero: "))

        print(f"La divicion da: {num1 / num2}")

    case _:
        print("Operacion invalido")

print("Tercer ejercicio: For loop")

num3 = int(input("Ingrese un numero: "))
for i in range(0, 11):
    print(f"{num3} * {i} = {num3*i}")