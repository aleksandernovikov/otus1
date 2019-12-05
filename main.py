from functools import wraps
from random import sample
from string import ascii_letters


def args_doc_result(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        func_result = func(*args, **kwargs)
        print(func.__doc__.strip())
        print(f'{func_result} = {func.__name__}{args}\n')
        return func_result

    return wrapped


@args_doc_result
def list_sum(list1: list, list2: list) -> list:
    """
    Объедините 2 списка так, чтобы в итоге получился 1 список включающий элементы обоих
    """
    return list1 + list2


l1 = [1, 3, 6, 8]
l2 = [9, 0, 5, 3]

result = list_sum(l1, l2)


@args_doc_result
def wo_dupe(input_list: list) -> list:
    """
    Удалите дубликаты из списка
    """
    return list(set(input_list))


wo_dupe(result)


@args_doc_result
def my_count(input_list: list) -> dict:
    """
    Посчитайте количество символов в списке и выведите цифры. A: 5, B: 3, C: 1
    """
    return {el: input_list.count(el) for el in set(input_list)}


d1 = [l for l in "".join(['A' * 5, 'B' * 3, 'C'])]
my_count(d1)


@args_doc_result
def is_palindrome(word: str) -> bool:
    """
    Сделайте проверку, явдяется ли слово Палиндромом
    """
    return word == word[::-1]


is_palindrome('abba')


@args_doc_result
def dif(list1: list, list2: list) -> list:
    """
    На вход получаете 2 списка, выведите новый список с элементами первого, которых нет во втором
    """
    return list(set(list1) - set(list2))


nl1, nl2 = sample(ascii_letters, 5), sample(ascii_letters, 15)
dif(nl1, nl2)


@args_doc_result
def repetitive(string: str) -> bool:
    """
    Проверьте, повторяются ли символы в строке
    """
    for symbol in string:
        if string.count(symbol) > 1:
            return True
    return False


repetitive('samba')


@args_doc_result
def frequent_and_rare(string: str) -> tuple:
    """
    Найдите и выведите наиболее и наимее часто встречающеся слова в строке
    """
    wc = my_count(string.split())
    min_count, max_count = min(wc.values()), max(wc.values())
    return [w for w, c in wc.items() if c is max_count], [w for w, c in wc.items() if c is min_count]


frequent_and_rare('Найдите и выведите наиболее и наимее часто встречающеся слова в строке')
