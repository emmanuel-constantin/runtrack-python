def my_len(phrase):
    count = 0
    for i in phrase:
        count += 1
    return count

def my_long_word(n,phrase):
    current_word = ""
    long_words = []
    long_words2 = ""
    for i in range(my_len(phrase)):
        if phrase[i] != " ":
            current_word += phrase[i]
        else:
            if my_len(current_word) > n:
                long_words += [current_word]
            current_word = " "
    for i in range (my_len(long_words)):
        long_words2 += long_words[i]
    return long_words2
    


print(my_long_word(3, "La peur est le chemin vers le côté obscur la peur mène à la colère la colère mène à la haine la haine mène à la souffrance"))
