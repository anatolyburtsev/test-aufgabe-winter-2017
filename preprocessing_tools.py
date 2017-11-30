import re
import numpy as np
import pymorphy2

ENABLE_MORPHING = False

morph = pymorphy2.MorphAnalyzer()

# clean_up("a1;😘2л  д") -> 'a12л д'
def clean_up(sentence):
    debug = False
    if debug: print("input clean_up: " + sentence)
    sentence = sentence.lower()
    cleaned_sentence = re.sub("  ", " ", re.sub("[^a-zа-яё0-9 ]", " ", sentence))
    if debug: print("after clean_up: " + cleaned_sentence)
    return cleaned_sentence

def to_normal_form(word):
    if not ENABLE_MORPHING: 
        return word
    debug = False
    normal_form = morph.parse(word)[0].normal_form
    if debug: print("before norm: " + str(word) + ". after: " + str(normal_form))
    return normal_form

def split_transform(sentence):
    words = sentence.split(" ")
    words = list(map(to_normal_form, words))
    words = [x for x in words if x != ""] 
    return " ".join(words)

def prepare_processing_sentence(sentence):
    debug = 0
    if debug: print("input prep_proc: " + str(sentence))
    if type(sentence) != type("abc") and type(sentence) != np.str_:
        if len(sentence) > 1:
            raise Exception("smth went wrong! type: " + str(type(sentence)) + " input: " + str(sentence) )
        else:
            sentence = sentence[0]
    if debug: print("extracted str: " + str(sentence))
    clean_sentence = clean_up(sentence)
    if debug: print("cleaned: " + clean_sentence)
    return split_transform(clean_sentence)

def prepare_processing(X_input):
    X_out = list()
    for i in range(len(X_input)):
        sentence = prepare_processing_sentence(X_input[i])
        X_out.append(sentence)
    X_out = np.array(X_out)
    return X_out
