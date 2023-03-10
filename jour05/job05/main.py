xmarches = int(input("Nombre de marches ? "))
ycm = int(input("Taille des marches ? "))
hauteurtotale = 0

def hauteurParcourue(x, y):
    hauteurtotale = (((x * y)*2)*7)/100
    print("Pour", x, " marches de ", y, " cm, il parcourt ", hauteurtotale, "m par semaine.")

hauteurParcourue(xmarches, ycm)