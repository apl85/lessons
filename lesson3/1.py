# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию,
# необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.


slovar = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
          'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'
}
def eng_to_rus(word):
    return slovar.get(word)

print(eng_to_rus('ten'))

# (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать
# корректную работу с числительными, начинающимися с заглавной буквы — результат тоже
# должен быть с заглавной. Например:



slovar = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
          'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'
}
def eng_to_rus(word):
    if word[0].isupper():
        word = word.lower()
        return slovar[word].capitalize()
    else:
        return slovar.get(word)
print(eng_to_rus('Ten'))
print(eng_to_rus('ten'))