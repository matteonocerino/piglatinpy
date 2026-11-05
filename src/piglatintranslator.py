from src.error import PigLatinError

def first_index_of_vowel(word):
    found = False
    i = 0
    while not found and i < len(word):
        letter = word[i]
        if letter in "aeiou":
            found = True
        else:
            i += 1
    return i

def translate_word(word):
    first_letter = word[0]
    if first_letter in "aeiou":
        last_letter = word[-1]
        if last_letter in "aeiou":
            return word + "yay"
        if last_letter == "y":
            return word + "nay"
        return word + "ay"
    i = first_index_of_vowel(word)
    first_part = word[:i]
    second_part = word[i:]
    return second_part + first_part + "ay"

def translate_punctuated_word(word):
    last_character = word[-1]
    if last_character in ".,;:?!()":
        return translate_word(word[:-1]) + last_character
    if not last_character.isalpha():
        raise PigLatinError()
    return translate_word(word)

def translate_words(words, separator):
    translated_words = []
    for word in words:
        translated_words.append(translate_punctuated_word(word))
    return separator.join(translated_words)

class PigLatinTranslator:

    def __init__(self, phrase: str):
        """
        Creates a pig latin translator given a phrase.
        :param phrase: the phrase.
        :raise PigLatinError: for any error situation.
        """
        self.phrase = phrase

    def get_phrase(self) -> str:
        """
        Returns the phrase.
        :return: the phrase.
        """
        return self.phrase

    def translate(self) -> str:
        """
        Returns the Pig Latin translation of the phrase.
        :return: the translation.
        """
        if self.phrase == "":
            return "nil"

        if "-" in self.phrase:
            return translate_words(self.phrase.split("-"), "-")

        if " " in self.phrase:
            return translate_words(self.phrase.split(), " ")

        return translate_punctuated_word(self.phrase)