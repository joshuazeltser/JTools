def to_lower_case(string):
    return string.lower()


def to_upper_case(string):
    return string.upper()


def reverse_string(string):
    return string[::-1]


def word_count(string):
    words = string.split()

    return len(words)


def char_count(string):
    return len(string)


def split_string_by(string, char):
    return string.split(char)


def word_occurence_count(string):
    words = string.split()

    dict = {}

    for x in range(0, len(words)):
        dict[words[x]] = words.count(words[x])

    return str(dict)
