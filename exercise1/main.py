from itertools import permutations as perm
from os import path


def annograms(word: str):
    """Anagrams finder"""
    # Changing the list comprehenion sugested by the exercise to a set we
    # can eliminate the repeated elemnts if any and makes the lookups much faster.
    words = {w.rstrip() for w in open(path.join(path.dirname(__file__), "WORD.lst"))}
    sep_word = list(word)
    words_in_list = set()

    for permutation in perm(sep_word):
        permutation = "".join(permutation)
        if permutation in words:
            words_in_list.add(permutation)

    return list(words_in_list)


if __name__ == "__main__":
    print(annograms("train"))
    print("--")
    print(annograms("drive"))
    print("--")
    print(annograms("python"))
    print("--")
    print(annograms("staring"))


# It was singifantly slower when I ran the functions with lists
