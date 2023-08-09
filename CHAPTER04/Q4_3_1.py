# names = ("a", "b", "c")
# sep = "_"
# sep.join(names)


def concat_words(*args, separator="_"):
    """"4_choume", "Minatoku", "Tokyo", "Japan", separator=""" ""
    return separator.join(args)


concat_words("a", "b", "c", "d", separator="_")
concat_words("4_choume", "Minatoku", "Tokyo", "Japan", separator="")
print()
print(concat_words(""))
# def join_words(*words, separator="_"):
# return separator.join(words)


# words_joined = join_words("a", "b", "c", "d", separator="_")
# print(words_joined)
