def my_len(liste):
    count = 0
    for i in liste:
        count += 1
    return count

def tri_liste(liste):
    n = my_len(liste)
    for n in range (1, n):
        cle = liste[n]
        j = n-1
        while j >= 0 and L[j]>cle:
            liste[j+1] = liste[j]
            j -= 1
        liste[j+1] = cle
    return liste

L = [8,6,4,3]
print(tri_liste(L))
    