
# 1. Utworzenie funkcji 2^N iteracyjnej.
#    n - liczba całkowita.
def getPoweredTwo_ITERATIVE(n):
    value = 2
    for i in range(1, n):
        value *= 2
    return value;

# 2. Utworzenie funkcji 2^N rekurencyjnej.
#   n - liczba całkowita.
def getPoweredTwo_RECURSIVE(n):
    if n == 1:
        return 2
    else:
        return 2*getPoweredTwo_RECURSIVE(n-1)

# 3. Utworzenie funkcji, która będzie testowała rekurencyjną wersję potęgowania 2.
def testGetPoweredTwo_RECURSIVE(n):
    print("Testing recursive version for", n)
    for i in range(1, n+1):
        print(i, " test: ", getPoweredTwo_RECURSIVE(i))

# 4. Utworzenie funkcji, która będzie testowała iteracyjną wersję potęgowania 2.
def testGetPoweredTwo_ITERATIVE(n):
     print("Testing iterative version for", n)
     for i in range(1, n+1):
         print(i, " test: ", getPoweredTwo_ITERATIVE(i))
         
# 5. Testowanie iteracyjnej funkcji.
testGetPoweredTwo_ITERATIVE(5)

# 6. Testowanie rekurencyjnej funkcji.
testGetPoweredTwo_RECURSIVE(5)

# Autor: Juliusz Łosiński 46155
