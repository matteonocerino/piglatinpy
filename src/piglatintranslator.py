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
            words = self.phrase.split("-")

            translated_words = []

            for word in words:
                translated_words.append(translate_word(word))

            return "-".join(translated_words)

        if " " in self.phrase:
            words = self.phrase.split()

            translated_words = []

            for word in words:
                translated_words.append(translate_word(word))

            return " ".join(translated_words)

        return translate_word(self.phrase)