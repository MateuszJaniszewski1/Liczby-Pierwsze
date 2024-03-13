def funkcja(liczba):
    if liczba <= 1:
        return False
    if liczba <= 3:
        return True
    if liczba % 2 == 0 or liczba % 3 == 0:
        return False
    i = 5
    while i * i <= liczba:
        if liczba % i == 0 or liczba % (i + 2) == 0:
            return False
        i += 6
    return True

a = int(input("Podaj liczbę do sprawdzenia: "))
if funkcja(a):
    print(f"{a} jest liczbą pierwszą.")
else:
    print(f"{a} nie jest liczbą pierwszą.")