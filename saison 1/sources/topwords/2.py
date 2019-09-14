def split_fragments(text):
    res = list()
    for fragment in contents.split():
        if "’" in fragment:
            (before, after) = fragment.split("’")
            res.append(before)
            res.append(after)
        else:
            res.append(fragment)
    return res


def clean_fragment(fragment):
    result = ""
    for c in fragment:
        if c.isalpha() or c in ["-", "'"]:
            result += c

    return result


def split_words(text):
    fragments = split_fragments(text)
    res = list()
    for fragment in fragments:
        fragment = fragment.lower()
        fragment = clean_fragment(fragment)
        if fragment:
            res.append(fragment)
    return res


contents = "L’univers est, peut-être, « infini! »"
words = split_words(contents)
print(words)
