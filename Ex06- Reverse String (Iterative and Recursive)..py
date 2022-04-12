# 1. Utworzenie funkcji do odwracania ciągu znaków - wersja iteracyjna.
def reverse_iterative(label):
    reversed_label="";
    j=len(label)-1
    for i in range(len(label)):
        reversed_label+=label[j]
        j-=1
    return reversed_label

# 2. Utworzenie funkcji do odwracania ciągu znaków - wersja rekurencyjna.
def reverse_recursive_helper(src, res, pos):
    if(pos < 0):
        return res
    else:
        return reverse_recursive_helper(src, res+src[pos]+"", pos-1)

def reverse_recursive(label):
    return reverse_recursive_helper(label, "", len(label)-1)
    

# 3. Testowanie funkcji do odwracania ciągu znaków.
def test_reverse(type):
    labels=["TEST", "UMG", "JULEK", "BATMAN", "HOTDOG", "PIZZA", "PYTHON"]
    print()
    if(type=="iterative"):
        print("Testing iterative version: -------------]")
    else:
        print("Testing recursive version: -------------]") 
    for i in labels:
        print()
        print("Before: ", i)
        if(type=="iterative"):
            print("After: ", reverse_iterative(i))
        else:
            print("After: ", reverse_recursive(i))


# 4. Wywolanie testowania.
test_reverse("iterative")
test_reverse("recursive")

# Autor: Juliusz Łosiński 46155
