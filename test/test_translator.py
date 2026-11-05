from unittest import TestCase
from src.piglatintranslator import PigLatinTranslator

class TestPigLatinTranslator(TestCase):

    def test_get_phrase(self):
        translator = PigLatinTranslator("hello world")
        phrase = translator.get_phrase()
        self.assertEqual("hello world", phrase)

    def test_translate_empty_phrase(self):
        translator = PigLatinTranslator("")
        translation = translator.translate()
        self.assertEqual("nil", translation)

    def test_translate_word_starting_vowel_a_ending_y(self):
        translator = PigLatinTranslator("any")
        translation = translator.translate()
        self.assertEqual("anynay", translation)

    def test_translate_word_starting_vowel_e_ending_y(self):
        translator = PigLatinTranslator("enemy")
        translation = translator.translate()
        self.assertEqual("enemynay", translation)

    def test_translate_word_starting_vowel_ending_vowel(self):
        translator = PigLatinTranslator("apple")
        translation = translator.translate()
        self.assertEqual("appleyay", translation)

    def test_translate_word_starting_vowel_ending_consonant(self):
        translator = PigLatinTranslator("ask")
        translation = translator.translate()
        self.assertEqual("askay", translation)

    def test_translate_word_starting_consonant(self):
        translator = PigLatinTranslator("hello")
        translation = translator.translate()
        self.assertEqual("ellohay", translation)