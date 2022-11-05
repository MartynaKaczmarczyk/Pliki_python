import unittest

n = int(input("Wpisz swoją liczbę całkowitą dodatnią: "))
g = "*"
spacja = " "
for i in range(n):
    print(spacja * (n - i) + g * i + "*" + g * i + spacja * (n - 1))
    i += 1

print(spacja * (n - 1) + "|_|")"""
