# 1. Utworzenie funkcji służącej do szyfrowania ciągu znaków
#    przy pomocy szyfru Cezara oraz podanego klucza (przesunięcie).
#    WERSJA ITERACYJNA
def cipher_iterative(txt, key):
    res=""
    txt=txt.upper()
    for i in range(len(txt)):
        intValue = ord(txt[i])
        if (intValue + key >= 90):
            intValue = (intValue+key)% 90
        else:
            intValue += key
        res+=chr(intValue)
    return res

# 2. Utworzenie funkcji służącej do deszyfrowanai ciągu znaków.
#    przy pomocy szyfru cezara oraz podanego klucza (przesunięcie).
#    WERSJA ITERACYJNA
def decipher_iterative(txt, key):
    res=""
    lb = 65
    rb = 90
    for i in txt:
        intValue = ord(i)
        diff= intValue - key
        if(diff<lb):
            intValue -= diff %rb
        else:
            intValue = intValue - key
        res+=chr(intValue)
    return res;
    
# 2. Utworzenie funkcji służącej do szyfrowania ciągu znaków
#    przy pomocy szyfru Cezara oraz podanego klucza (przesunięcia).
def cipher_recursive(txt, key):
    return cipher_recursive_helper(txt, key, 0, "")

def cipher_recursive_helper(txt, key, pos, res):
    if(pos >= len(txt)):
        return res
    intValue = ord(txt[pos])
    if(intValue + key >=90):
        intValue = (intValue+key)%90
    else:
        intValue +=key
    return cipher_recursive_helper(txt, key, pos+1, res+chr(intValue))

# 3. Utworzenie funkcji służącej do deszyfrowania ciągu znaków.
#    przy pomocy szyfru cezara oraz podanego klucza (przesunięcie).
#    WERSJA REKURENCYJNA
def decipher_recursive(txt, key):
    return decipher_recursive_helper(txt, key, 0, "")

def decipher_recursive_helper(txt, key, pos, res):
    if(pos>=len(txt)):
        return res
    intValue = ord(txt[pos])
    diff=intValue-key
    if(diff<65):
        intValue-=diff % 90
    else:
        intValue = intValue - key
    return decipher_recursive_helper(txt, key, pos+1, res+chr(intValue))

# 4. Utworzenie funkcji do testowania szyfrowania.
def test_cipher(type):
    data=["TEST", "KOT", "BATMAN", "SPIDERMAN", "SUPERMAN"]
    key=3
    print(" ")
    print("& Encrypting: &")
    if(type=="iterative"):
        print("Testing iterative version: ")
    else:
        print("Testing recursive version: ")
    for i in data:
        if (type == "iterative"):
            print("Before: ", i)
            print("After: ", cipher_iterative(i, key))
        else:
            print("Before: ", i)
            print("After: ", cipher_recursive(i, key))

# 4. Utworzenie funkcji do testowania deszyfrowania.
def test_decipher(type):
    data=["WHVW", "NRW", "EDWPDQ", "VSLGHUPDQ", "VXSHUPDQ"]
    key=3
    print(" ")
    print("# Decrypting:  #")
    if(type=="iterative"):
        print("Testing iterative version: ")
    else:
        print("Testing recursive version: ")
    for i in data:
        if (type == "iterative"):
            print("Before: ", i)
            print("After: ", decipher_iterative(i, key))
        else:
            print("Before: ", i)
            print("After: ", decipher_recursive(i, key))                  

# 4. Testowanie.
test_cipher("iterative")
test_cipher("recursive")
test_decipher("iterative")
test_decipher("recursive")

# Autor: Juliusz Łosiński 46155


