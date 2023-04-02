# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

# def remove_exclamation_marks(s):
#     return(s.split('!'))
# s = input('Введите строку: ')
# ans = "".join(remove_exclamation_marks(s))
# print(ans)       

# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

# def remove_last_em(s):
#     if s[-1] == '!':
#         s.remove(s[-1])
#     return(s)
# s = list(input('Введите строку: '))
# ans = "".join(remove_last_em(s))
# print(ans)       

# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    tmp = []
    for i in range(len(s)):
        if s[i].count("!") != 1:
            tmp.append(s[i])
    return(tmp)
    
s = input('Введите строку: ').split(" ")
tmp = " ".join(remove_word_with_one_em(s))
print(tmp)
