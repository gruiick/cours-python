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


contents = "L’univers est, peut-être, « infini! »"
fragments = split_fragments(contents)
print(fragments)
