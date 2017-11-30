def find_stop_words_dataframe(text_data, column_name):
    # dicts with amount of words
    dicts_list = [dict(), dict(), dict(), dict()]
    for index, row in text_data.iterrows():
        c_id = find_cat(row["category_id"])
        for word in row[column_name].split(" "):
            add2dict(dicts_list[c_id], word)
    return calculate_common_words(dicts_list)


def find_stop_words_array(text_array, categories_list):
    # dicts with amount of words
    dicts_list = [dict(), dict(), dict(), dict()]
    for i in range(len(text_array)):
        c_id = categories_list[i]
        for word in text_array[i].split(" "):
            add2dict(dicts_list[c_id], word)
    return calculate_common_words(dicts_list)


def calculate_common_words(dicts_list):
    common_words = dict()
    common_words_list = list()

    for d in dicts_list:
        s = [(k, d[k]) for k in sorted(d, key=d.get, reverse=True)]
        for k, v in s[:50]:
            add2dict(common_words, k)
    for k,v in common_words.items():
        if v >= 3:
            common_words_list.append(k)
    return common_words_list


def find_cat(number):
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
    if not value in dictname:
        dictname[value] = 1
    else:
        dictname[value] += 1
