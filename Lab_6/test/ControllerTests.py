import unittest
from Controller import Controller
from Domain import Word, WordType, Phrase
from Repository import FileService


class ControllerTests(unittest.TestCase):
    __controller = Controller.Controller()

    def test_generate_phrases(self):
        no_of_phrases = 3
        self.__controller.generate_phrases(no_of_phrases)
        phrases = FileService.PhraseFileService.read_phrases()
        self.assertEqual(no_of_phrases, len(phrases))

    def test_get_correct_phrases(self):
        word_1 = Word.Word("preia", WordType.WordType.VERB)
        word_2 = Word.Word("afacerea", WordType.WordType.NOUN)
        word_3 = Word.Word("mare", WordType.WordType.ADJECTIVE)
        phrase_1 = Phrase.Phrase()
        phrase_1.add_word(word_1)
        phrase_1.add_word(word_2)
        phrase_1.add_word(word_3)
        word_4 = Word.Word("canta", WordType.WordType.VERB)
        word_5 = Word.Word("cantaretul", WordType.WordType.NOUN)
        word_6 = Word.Word("vestit", WordType.WordType.ADJECTIVE)
        phrase_2 = Phrase.Phrase()
        phrase_2.add_word(word_4)
        phrase_2.add_word(word_5)
        phrase_2.add_word(word_6)
        self.__controller.repo.phrases.add(phrase_1)
        self.__controller.repo.phrases.add(phrase_2)
        working = False
        check_1 = False
        check_2 = False
        correct_phrases = self.__controller.get_correct_phrases()
        for phrase in correct_phrases:
            if phrase.__eq__(phrase_1):
                check_1 = True
            if phrase.__eq__(phrase_2):
                check_2 = True
        if check_1 and check_2:
            working = True
        self.assertEqual(working, True)

    def test_get_correct_phrases_1(self):
        word_1 = Word.Word("preia", WordType.WordType.VERB)
        word_2 = Word.Word("preia", WordType.WordType.VERB)
        word_3 = Word.Word("preia", WordType.WordType.VERB)
        phrase_1 = Phrase.Phrase()
        phrase_1.add_word(word_1)
        phrase_1.add_word(word_2)
        phrase_1.add_word(word_3)
        word_4 = Word.Word("canta", WordType.WordType.VERB)
        word_5 = Word.Word("cantaretul", WordType.WordType.NOUN)
        word_6 = Word.Word("vestit", WordType.WordType.ADJECTIVE)
        phrase_2 = Phrase.Phrase()
        phrase_2.add_word(word_4)
        phrase_2.add_word(word_5)
        phrase_2.add_word(word_6)
        self.__controller.repo.phrases.add(phrase_1)
        self.__controller.repo.phrases.add(phrase_2)
        working = False
        check_1 = True
        check_2 = False
        correct_phrases = self.__controller.get_correct_phrases()
        for phrase in correct_phrases:
            if phrase.__eq__(phrase_1):
                check_1 = False
            if phrase.__eq__(phrase_2):
                check_2 = True
        if check_1 and check_2:
            working = True
        self.assertEqual(working, True)

    def test_word_in_list(self):
        word_1 = Word.Word("preia", WordType.WordType.VERB)
        word_2 = Word.Word("afacerea", WordType.WordType.NOUN)
        word_3 = Word.Word("mare", WordType.WordType.ADJECTIVE)
        phrase_1 = Phrase.Phrase()
        phrase_1.add_word(word_1)
        phrase_1.add_word(word_2)
        phrase_1.add_word(word_3)
        self.assertEqual(1, self.__controller.word_in_list("preia", phrase_1.get_words()))

    def test_word_in_list_1(self):
        word_1 = Word.Word("preia", WordType.WordType.VERB)
        word_2 = Word.Word("afacerea", WordType.WordType.NOUN)
        word_3 = Word.Word("mare", WordType.WordType.ADJECTIVE)
        phrase_1 = Phrase.Phrase()
        phrase_1.add_word(word_1)
        phrase_1.add_word(word_2)
        phrase_1.add_word(word_3)
        self.assertEqual(0, self.__controller.word_in_list("", phrase_1.get_words()))

    def test_word_in_list_2(self):
        word_1 = Word.Word("preia", WordType.WordType.VERB)
        word_2 = Word.Word("preia", WordType.WordType.VERB)
        word_3 = Word.Word("preia", WordType.WordType.VERB)
        phrase_1 = Phrase.Phrase()
        phrase_1.add_word(word_1)
        phrase_1.add_word(word_2)
        phrase_1.add_word(word_3)
        self.assertEqual(3, self.__controller.word_in_list("preia", phrase_1.get_words()))
