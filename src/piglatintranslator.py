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

        first_letter = self.phrase[0]
        if first_letter in "aeiou":
            last_letter = self.phrase[len(self.phrase) - 1]
            if last_letter in "aeiou":
                return self.phrase + "yay"
            if last_letter in "y":
                return self.phrase + "nay"
            return self.phrase + "ay"

        i = first_index_of_vowel(self.phrase)
        first_part = self.phrase[0:i]
        second_part = self.phrase[i:]
        return second_part + first_part + "ay"