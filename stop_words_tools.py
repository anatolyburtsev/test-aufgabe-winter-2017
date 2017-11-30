def find_stop_words_dataframe(text_data, column_name):
    # same as next function, differ in input params
    # dicts with amount of words
    dicts_list = [dict(), dict(), dict(), dict()]
    for index, row in text_data.iterrows():
        c_id = find_cat(row["category_id"])
        for word in row[column_name].split(" "):
            add2dict(dicts_list[c_id], word)
    return calculate_common_words(dicts_list)


def find_stop_words_array(text_array, categories_list):
    """
    >>> find_stop_words_array(["hello guys", "hello avito", "hello moscow", "hello onotole11pewpew"], [1,1,2,3])
    ['hello']

    :param text_array:
    :param categories_list:
    :return: dicts with count of words
    """
    dicts_list = [dict(), dict(), dict(), dict()]
    for i in range(len(text_array)):
        c_id = categories_list[i]
        for word in text_array[i].split(" "):
            add2dict(dicts_list[c_id], word)
    return calculate_common_words(dicts_list)


def calculate_common_words(dicts_list):
    """" Return the most frequent words, appeared in 3 or more dicts == categories

    >>> calculate_common_words([{"a":5, "b": 2},{"a": 5, "b": 3}, {"b": 10, "c": 1}, {"d": 100}])
    ['b']
    """
    common_words = dict()
    common_words_list = list()

    for d in dicts_list:
        s = [(k, d[k]) for k in sorted(d, key=d.get, reverse=True)]
        for k, v in s[:50]:
            add2dict(common_words, k)
    for k, v in common_words.items():
        if v >= 3:
            common_words_list.append(k)
    return common_words_list


def find_cat(number):
    """
    Return uber category (0 to 3) by particular category (1 to 53)

    >>> find_cat(14)
    0
    """
    if number < 15:
        return 0
    if number < 30:
        return 1
    if number < 42:
        return 2
    if number < 54:
        return 3
    raise Exception("Category id exceed limit: " + str(number))


def add2dict(dictname, value):
    """
    >>> add2dict({}, "test")
    {'test': 1}
    >>> add2dict({'test': 1}, "test")
    {'test': 2}

    :param dict:
    :param value:
    :return: dict
    """
    if value not in dictname:
        dictname[value] = 1
    else:
        dictname[value] += 1
    return dictname


if __name__ == "__main__":
    import doctest

    doctest.testmod()
