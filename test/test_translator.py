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

    def test_translate_word_starting_consonant_h(self):
        translator = PigLatinTranslator("hello")
        translation = translator.translate()
        self.assertEqual("ellohay", translation)

    def test_translate_word_starting_consonant_w(self):
        translator = PigLatinTranslator("word")
        translation = translator.translate()
        self.assertEqual("ordway", translation)

    def test_translate_word_starting_two_consonants(self):
        translator = PigLatinTranslator("known")
        translation = translator.translate()
        self.assertEqual("ownknay", translation)

    def test_translate_word_starting_three_consonants(self):
        translator = PigLatinTranslator("street")
        translation = translator.translate()
        self.assertEqual("eetstray", translation)

    def test_translate_phrase_containing_two_words(self):
        translator = PigLatinTranslator("hello world")
        translation = translator.translate()
        self.assertEqual("ellohay orldway", translation)