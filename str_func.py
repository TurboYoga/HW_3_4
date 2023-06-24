def foo(words):
    '''функция увеличения слова'''
    return words.upper()


def foo2 (word):
    '''Докстринг'''
    word_1 = word.split()
    result = []
    for a in word_1:
        result.append(a.capitalize())
    return ' '.join(result)

