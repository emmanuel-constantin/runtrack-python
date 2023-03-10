def isrectangle(a,b,c):
    if (a * a) == (b * b)+(c * c):
        print("Triangle rectangle")
    else:
        print("pas rectangle")

def isisocele(a,b,c):
    if a == b or a == c or b == c:
        return "triangle isocele"
    else:
        return "pas isocele"

def istriangle(a,b,c):
    if c < a > b:
        if a < (b + c):
            isrectangle(a,b,c)
            print(isisocele(a,b,c))
        else:
            print("pas triangle")
    elif c < b > a:
        if b < (a + c):
            isrectangle(b,a,c)
            print(isisocele(b,a,c))
        else:
            print("pas triangle")
    elif b < c > a:
        if c < (b + a):
           isrectangle(c,a,b)
           print(isisocele(c,a,b))
        else:
            print("pas triangle")

istriangle(3,5,4)

