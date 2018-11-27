import random

def main():
    VOWELS = "aeiou"
    CONSONANTS = "bcdfghjklmnpqrstvwxyz"

    word_format = "ccvcvvc"
    word = ""
    word = generate_word(CONSONANTS, VOWELS, word, word_format)

    print(word)


def generate_word(CONSONANTS, VOWELS, word, word_format):
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
    return word

