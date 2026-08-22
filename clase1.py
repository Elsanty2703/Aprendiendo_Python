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