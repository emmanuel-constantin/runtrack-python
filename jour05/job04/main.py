def decale_message(message):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    message_decale = ''
    
    for lettre in message:
        if lettre.lower() not in alphabet: # si la lettre n'est pas dans l'alphabet, on la conserve telle quelle
            message_decale += lettre
        else:
            indice = alphabet.index(lettre.lower())
            indice_decale = (indice + 3) % 26
            lettre_decalee = alphabet[indice_decale]
            
            if lettre.isupper():
                lettre_decalee = lettre_decalee.upper()
            
            message_decale += lettre_decalee
    return message_decale
print(decale_message("abcd efgz"))