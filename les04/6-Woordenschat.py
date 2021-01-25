def getWoorden(line):  # line, bv "Hallo, dit is een string.\nDit is een nieuwe lijn."
    from string import punctuation
    words = line.split()  # words in line, bv. ["Hallo," , "dit", "is", ...]
    clean_words = set()  # lege set
    for word in words:  # doorloop elk woord in words (bv. eerst "Hallo,", dan "dit", dan...)
        # voeg toe aan de lege set: het woord, zonder hoofdletters, zonder leestekens
        clean_words.add(word.lower().strip(punctuation))

    return clean_words


def leesBestand(name):
    with open(name) as file:
        text = file.read()
    file.close()

    return text.split("\n")


def add_to_wordcount(word, dictionary):
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1
    return dictionary


# [FIXED] Fault in the program: prints amount of *new* words instead of total found words
# [FIXED] Fault 2: prints all words found in line instead of only new
def main():
    filename = input("Name of file:\n> ")
    words = set()
    wordcount = dict()
    for line in leesBestand(filename):
        print("-=-=-=-=-=-=-=-=-=-=- NEXT -=-=-=-=-=-=-=-=-=-=-")
        print("Verwerkte zin:", line)
        new_words = getWoorden(line)
        print("Grootte van de nieuwe woordenschat:", len(words.union(new_words)))
        print("Nieuwe woorden toegevoegd:", new_words.difference(words))
        words.update(new_words)  # basically the same as union, however, this does not return a value.
        for word in words:
            if word in new_words:
                wordcount = add_to_wordcount(word, wordcount)
    print("|||||||||||||||||||| KLAAR ||||||||||||||||||||")

    more_than_half = set()
    for word, amount in wordcount.items():
        if amount > len(leesBestand(filename)) // 2:
            more_than_half.add(word)

    print("Woorden die in meer dan 50% van de zinnen voorkomen:\n", more_than_half)

    return words


main()