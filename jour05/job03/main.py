
def tapis(n):
    print("+" + "-" * (n) + "+")
    strligne = ""
    for i in range (0, n - 9):
        for j in range (0, n+1):
            print("|" + "#" * (n) + "|")
            if i == j :
                for k in range (len(strligne)):
                    strligne[i]
            elif i+j == n:
                print(" ", end=" ")
            else:
                print("#", end=" ")

    print("+" + "-" * (n) + "+")
tapis(10)