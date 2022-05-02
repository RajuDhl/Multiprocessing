string_one = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'a', 'c', 'e']
string_two = ['a', 'f', 'c', 'h', 'e', 'i', 'g']


def listify_companies(one, two):
    index = {req_word: [idx for idx, word in enumerate(one) if word == req_word] for idz, req_word in
             enumerate(two)}
    test = [[word for idx, word in enumerate(one) if word == word2 and [word2] not in []] for idz, word2 in enumerate(two)]

    return test


print(listify_companies(string_one, string_two))


def common_letters(string_one, string_two):
    common = []
    for i in string_one:
        if i in string_two:
            if i not in common:
                common.append(i)
    return common


# print(common_letters(string_one, string_two))
