n = int(input("Wpisz liczbę pobieranych liczb: "))
suma = 0
for i in range(n):
    m = float(input("Twoja liczba: "))
    suma = suma + m
sr = suma / n
print(sr)
