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

    def test_check_similarity_true(self):
        phrase = Phrase.Phrase()
        phrase.add_word(Word.Word("cana", WordType.WordType.NOUN))
        phrase.add_word(Word.Word("este", WordType.WordType.VERB))
        phrase.add_word(Word.Word("mare", WordType.WordType.ADJECTIVE))
        magic_phrase = Phrase.Phrase()
        magic_phrase.add_word(Word.Word("cana", WordType.WordType.NOUN))
        magic_phrase.add_word(Word.Word("este", WordType.WordType.VERB))
        magic_phrase.add_word(Word.Word("mare", WordType.WordType.ADJECTIVE))
        self.assertEqual(True, self.__controller.check_similarity(phrase, magic_phrase))

    def test_check_similarity_false(self):
        phrase = Phrase.Phrase()
        phrase.add_word(Word.Word("este", WordType.WordType.NOUN))
        phrase.add_word(Word.Word("cana", WordType.WordType.VERB))
        phrase.add_word(Word.Word("mare", WordType.WordType.ADJECTIVE))
        magic_phrase = Phrase.Phrase()
        magic_phrase.add_word(Word.Word("cana", WordType.WordType.NOUN))
        magic_phrase.add_word(Word.Word("este", WordType.WordType.VERB))
        magic_phrase.add_word(Word.Word("mare", WordType.WordType.ADJECTIVE))
        self.assertEqual(False, self.__controller.check_similarity(phrase, magic_phrase))

    def test_similarity_report_matching_words(self):
        phrase = Phrase.Phrase()
        phrase.add_word(Word.Word("este", WordType.WordType.VERB))
        phrase.add_word(Word.Word("cana", WordType.WordType.NOUN))
        phrase.add_word(Word.Word("mare", WordType.WordType.ADJECTIVE))
        magic_phrase = Phrase.Phrase()
        magic_phrase.add_word(Word.Word("cana", WordType.WordType.NOUN))
        magic_phrase.add_word(Word.Word("este", WordType.WordType.VERB))
        magic_phrase.add_word(Word.Word("mare", WordType.WordType.ADJECTIVE))
        self.__controller.repo.magic_phrases.add(magic_phrase)
        similarity_report = self.__controller.get_similarity_report(phrase, magic_phrase)
        working = True
        if similarity_report['similar_words'] != 3:
            working = False
        self.assertEqual(working, True)

    def test_similarity_report_2_matching_words(self):
        phrase = Phrase.Phrase()
        phrase.add_word(Word.Word("este", WordType.WordType.VERB))
        phrase.add_word(Word.Word("marul", WordType.WordType.NOUN))
        phrase.add_word(Word.Word("mare", WordType.WordType.ADJECTIVE))
        magic_phrase = Phrase.Phrase()
        magic_phrase.add_word(Word.Word("cana", WordType.WordType.NOUN))
        magic_phrase.add_word(Word.Word("este", WordType.WordType.VERB))
        magic_phrase.add_word(Word.Word("mare", WordType.WordType.ADJECTIVE))
        self.__controller.repo.magic_phrases.add(magic_phrase)
        similarity_report = self.__controller.get_similarity_report(phrase, magic_phrase)
        working = True
        if similarity_report['similar_words'] != 2:
            working = False
        self.assertEqual(working, True)

    def test_similarity_report_1_matching_words(self):
        phrase = Phrase.Phrase()
        phrase.add_word(Word.Word("preda", WordType.WordType.VERB))
        phrase.add_word(Word.Word("mare", WordType.WordType.ADJECTIVE))
        phrase.add_word(Word.Word("harta", WordType.WordType.NOUN))
        magic_phrase = Phrase.Phrase()
        magic_phrase.add_word(Word.Word("casa", WordType.WordType.NOUN))
        magic_phrase.add_word(Word.Word("este", WordType.WordType.VERB))
        magic_phrase.add_word(Word.Word("mare", WordType.WordType.ADJECTIVE))
        self.__controller.repo.magic_phrases.add(magic_phrase)
        similarity_report = self.__controller.get_similarity_report(phrase, magic_phrase)
        working = True
        if similarity_report['similar_words'] != 1:
            working = False
        self.assertEqual(working, True)

    def test_similarity_report_0_matching_words(self):
        phrase = Phrase.Phrase()
        phrase.add_word(Word.Word("zboara", WordType.WordType.VERB))
        phrase.add_word(Word.Word("marul", WordType.WordType.NOUN))
        phrase.add_word(Word.Word("mic", WordType.WordType.ADJECTIVE))
        magic_phrase = Phrase.Phrase()
        magic_phrase.add_word(Word.Word("cana", WordType.WordType.NOUN))
        magic_phrase.add_word(Word.Word("este", WordType.WordType.VERB))
        magic_phrase.add_word(Word.Word("mare", WordType.WordType.ADJECTIVE))
        self.__controller.repo.magic_phrases.add(magic_phrase)
        similarity_report = self.__controller.get_similarity_report(phrase, magic_phrase)
        working = True
        if similarity_report['similar_words'] != 0 and similarity_report['percentage'] != 0:
            working = False
        self.assertEqual(working, True)

