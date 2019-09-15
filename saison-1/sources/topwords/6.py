import sys


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


def split_fragments(text):
    res = list()
    for fragment in text.split():
        if "’" in fragment:
            before = fragment.split("’")[0]
            after = fragment.split("’")[1]
            res.append(before)
            res.append(after)
        else:
            res.append(fragment)
    return res


def get_frequencies(words):
    res = dict()
    for word in words:
        if word in res:
            res[word] += 1
        else:
            res[word] = 1
    return res


def get_scores(frequencies):
    res = list()
    for word, count in frequencies.items():
        res.append((count, word))
    res.sort(reverse=True)
    return res


def print_scores(scores):
    for count, word in scores:
        print(count, word)


def main():
    if len(sys.argv) < 2:
        sys.exit("not enough arguments")
    filename = sys.argv[1]
    file = open(filename)
    contents = file.read()
    words = split_words(contents)
    frequencies = get_frequencies(words)
    scores = get_scores(frequencies)
    top_words = scores[:20]
    print_scores(top_words)


main()
