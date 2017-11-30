import re
import numpy as np
import pymorphy2

ENABLE_MORPHING = True

morph = pymorphy2.MorphAnalyzer()


def clean_up(sentence):
    """
    Return cleaned string
    >>> clean_up("a1;😘2л        д")
    'a1 2л д'

    :param sentence:
    :return:
    """
    debug = False
    if debug: print("input clean_up: " + sentence)
    sentence = sentence.lower()
    cleaned_sentence = re.sub("[ ]+", " ", re.sub("[^a-zа-яё0-9 ]", " ", sentence))
    if debug: print("after clean_up: " + cleaned_sentence)
    return cleaned_sentence


def to_normal_form(word):
    """
    Return word in initial, normal form

    >>> to_normal_form("покупал")
    'покупать'
    """
    if not ENABLE_MORPHING: 
        return word
    debug = False
    normal_form = morph.parse(word)[0].normal_form
    if debug: print("before norm: " + str(word) + ". after: " + str(normal_form))
    return normal_form


def split_transform(sentence):
    """
    Return sentence with all words in normal forms
    >>> split_transform("Я покупал на avito")
    'я покупать на avito'

    :param sentence:
    :return:
    """
    words = sentence.split(" ")
    words = list(map(to_normal_form, words))
    words = [x for x in words if x != ""] 
    return " ".join(words)


def prepare_processing_sentence(sentence):
    """
    Return cleaned and transformed to normal form whole sentence
    >>> prepare_processing_sentence("Я покупал       на;;; avito😎😎🤩")
    'я покупать на avito'

    :param sentence:
    :return: cleaned and normalized sentence
    """
    debug = 0
    if debug: print("input prep_proc: " + str(sentence))
    if type(sentence) != str and type(sentence) != np.str_:
        if len(sentence) > 1:
            raise Exception("smth went wrong! type: " + str(type(sentence)) + " input: " + str(sentence) )
        else:
            sentence = sentence[0]
    if debug: print("extracted str: " + str(sentence))
    clean_sentence = clean_up(sentence)
    if debug: print("cleaned: " + clean_sentence)
    return split_transform(clean_sentence)


def prepare_processing(x_input):
    """
    Return cleaned and transformed to normal form list of sentences
    >>> prepare_processing(["Я покупал       на;;; avito😎😎🤩", "Очень был этому рад=)))🤠"]).tolist()
    ['я покупать на avito', 'очень быть это рад']

    :param list of sentences:
    :return list of processed sentences:
    """
    x_out = list()
    for i in range(len(x_input)):
        sentence = prepare_processing_sentence(x_input[i])
        x_out.append(sentence)
    x_out = np.array(x_out)
    return x_out


if __name__ == "__main__":
    import doctest

    doctest.testmod()