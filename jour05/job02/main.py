def draw_rectangle(width, height):
    # Affiche la première ligne avec des '-' pour le haut du rectangle
    print('|' + ('-' * (width/2)) + '|')
    
    # Affiche les lignes intérieures avec '|' sur les côtés et des espaces à l'intérieur
    for i in range(height-2):
        print('|' + ' '*(width-2) + '|')
    
    # Affiche la dernière ligne avec des '-' pour le bas du rectangle
    print('|' + ('-' * (width/2)) + '|')
draw_rectangle(10, 5)
        