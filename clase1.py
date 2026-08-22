name = "Santy"
print(f"Hola {name}")

print("1° ejercicio")
print("2° ejercicio")
print("3° ejercicio")
print("4° ejercicio")
print("0° terminar")
opc = int(input("Ingrese su opcion: "))

while opc != 0:

    match opc:
        case 1:
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

        case 2:
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
                        while (num2 == 0):
                            print("no se puede bobo")
                            num2 = int(input("Ingrese otro numero: "))

                    print(f"La divicion da: {num1 / num2}")

                case _:
                    print("Operacion invalido")

        case 3:
            print("Tercer ejercicio: For loop")

            num3 = int(input("Ingrese un numero: "))
            for i in range(11):
                print(f"{num3} * {i} = {num3 * i}")

        case 4:
            print("Cuarto ejercicio: while / breake-continue")
            dato = input("Ingrese su nombre: ")
            loop = 0

            while dato != name:
                if dato == name:
                    print("Adivinaste rey")
                else:
                    print("El nombre es incorrecto")
                    loop += 1

                if loop >= 5:
                    print("Como no te sabes tu nombre, coja oficio")
                    break

                dato = input("Ingrese su nombre: ")

        case 5:
            print("Quinto ejercicio: gauss")
            num4 = int(input("Ingrese un numero: "))
            num5 = 1
            for i in range((num4*2)+1):
                if i <= num4:
                    print('*' * i)
                else:
                    print('*' * (i-num5))
                    num5+=2

        case _:
            print("Fuerza leona")

    print("1° ejercicio")
    print("2° ejercicio")
    print("3° ejercicio")
    print("4° ejercicio")
    print("0° terminar")
    opc = int(input("Ingrese su opcion: "))