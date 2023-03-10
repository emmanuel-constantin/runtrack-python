def calcule(num1, operator, num2):
    resultat = 0
    if operator == '+':
        resultat = num1 + num2
    elif operator == '-':
        resultat = num1 - num2
    elif operator == '*':
        resultat = num1 * num2
    elif operator == '/':
        resultat = num1 / num2
    elif operator == '%':
        resultat = num1 % num2
    return resultat

num1 = 3
num2 = 3
operator = '*'
print(calcule(num1, operator,num2))