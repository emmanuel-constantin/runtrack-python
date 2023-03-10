ma_string = input("Entrez une chaîne de caractères, nous allons déterminer si elle contient la lettre e ")
i = 0
compt = 0
for i in range (len(ma_string)):
    if ma_string[i] == 'e':
        compt += 1
    i = i + 1
print ("votre chaine de caractères contient " + str(compt) + " fois la lettre e.")

