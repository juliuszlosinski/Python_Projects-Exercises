# 0. Załadowanie skryptów/ kodów źródłowych.
import random
import math

# 1. Utworzenie funkcji do obliczanie pierwiastków sumy kwadratów.
def mag(x, y):
    return math.sqrt(x*x + y*y)

# 2. Wywoływanie zdefniowanej funkcji dla 10 par losowych z [0, 10).
sum = 0
sumOfRoots = 0
n = 11
for i in range(1, n):
    # 2.1 Generowanie pierwszej oraz drugiej wartości.
    firstValue = random.random()*10
    secondValue = random.random()*10

    # 2.2 Obliczanie ich pierwiastku sumy kwadratów.
    roots = mag(firstValue, secondValue)

    # 2.3 Obliczanie dodatkowych parametrów (sumy).
    sum+=firstValue + secondValue
    sumOfRoots+=roots

    # 2.4 Wypisanie obecnej wartości pierwiastku sumy kwadratów dla pary.
    print(i, "pair: ", roots)
    
# 3. Wypisanie sumy elementów.
print("Sum of elements: ", sum);
print("Sum of ", n, " roots: ", sumOfRoots)

# Autor: Juliusz Łosiński 46155
