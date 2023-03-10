mot = input("Entrez une chaine de caracteres ")
i = (len(mot) - 1)
mot2 = ""
while i >= 0:
    mot2 += mot[i]
    i -= 1
print(mot2)