# 1. Utworzenie funkcji pokazującej liczby parzyste od a do b - ITERACYJNIE.
#    Warunki:
#    - a, b nalężą do zbioru liczb całkowitych,
#    - a < b,
def getEvens_ITERATIVE(a, b):
    buff=[]
    for i in range(a, b):
        if(i % 2 == 0):
            buff.append(i)
    return buff

# 2. Utworzenie funkcji pokazującej liczby parzyste od a do b - REKURENCYJNIE.
#    Warunki:
#    - a, b nalężą do zbioru liczb całkowitych,
#    - a < b,
def getEvens_RECURSIVE(a, b):
    buff = []
    getEvens_RECURSIVE_HELPER(buff, a, b)
    return buff
def getEvens_RECURSIVE_HELPER(buff, a, b):
    if( a == b):
        return
    if( a % 2 ==0):
        buff.append(a)
    getEvens_RECURSIVE_HELPER(buff, a+1, b)

# 3. Utworzenie funkcji do testowania iteracyjnej wersji.
def testEvens_ITERATIVE(a, b):
    print("Testowanie iteracyjnej wersji dla a = ", a, " i b = ", b, ":")
    buff = getEvens_ITERATIVE(a, b)
    for i in range(len(buff)):
        print(buff[i])

# 4. Utworzenie funkcji do testowania rekurencyjnej wersji.
def testEvens_RECURSIVE(a, b):
    print("Testowanie rekurencyjnej wersji dla a = ", a, " i b = ", b, ":")
    buff= getEvens_RECURSIVE(a, b)
    for i in range(len(buff)):
        print(buff[i])

# 5. Testowanie algorytmu.
a = 1
b = 25

# 5.1 Wersja iteracyjna.
testEvens_ITERATIVE(a, b)

# 5.2 Wersja rekurencyjna.
testEvens_RECURSIVE(a, b)

