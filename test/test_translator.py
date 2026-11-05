from unittest import TestCase
from src.translator import PigLatinTranslator
from src.error import PigLatinError

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

    def test_translate_composite_word(self):
        translator = PigLatinTranslator("well-being")
        translation = translator.translate()
        self.assertEqual("ellway-eingbay", translation)

    def test_translate_phrase_ending_with_exclamation_mark(self):
        translator = PigLatinTranslator("hello world!")
        translation = translator.translate()
        self.assertEqual("ellohay orldway!", translation)

    def test_translate_phrase_ending_with_question_mark(self):
        translator = PigLatinTranslator("hello world?")
        translation = translator.translate()
        self.assertEqual("ellohay orldway?", translation)

    def test_translate_word_with_invalid_punctuation(self):
        translator = PigLatinTranslator("hello@")
        self.assertRaises(PigLatinError, translator.translate)

    def test_translate_upper_case_word(self):
        translator = PigLatinTranslator("APPLE")
        translation = translator.translate()
        self.assertEqual("APPLEYAY", translation)

    def test_translate_title_case_word(self):
        translator = PigLatinTranslator("Hello")
        translation = translator.translate()
        self.assertEqual("Ellohay", translation)

    def test_translate_word_with_invalid_case(self):
        translator = PigLatinTranslator("biRd")
        self.assertRaises(PigLatinError, translator.translate)