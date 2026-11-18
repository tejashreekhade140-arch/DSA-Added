
def automorphicNumber(n):
    square = n * n

    if str(square).endswith(str(n)):
        print(n, "is an Automorphic Number")
    else:
        print(n, "is not an Automorphic Number")

automorphicNumber(25)
