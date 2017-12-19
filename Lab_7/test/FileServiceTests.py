import unittest
from Repository import FileService
from Domain import Word, Phrase, WordType


class FileServiceTests(unittest.TestCase):
    __wfs = FileService.WordFileService()
    __pfs = FileService.PhraseFileService()

    def test_word_file_service(self):
        word_repository = []
        word_1 = Word.Word("word_1", WordType.WordType.NOUN)
        word_2 = Word.Word("word_2", WordType.WordType.NOUN)
        word_repository.append(word_1)
        word_repository.append(word_2)
        self.__wfs.write_words(word_repository, WordType.WordType.NOUN)
        word_repository_test = self.__wfs.read_words(WordType.WordType.NOUN)
        working = True
        if len(word_repository) != len(word_repository_test):
            working = False
        for i in range(len(word_repository)):
            if not word_repository[i].__eq__(word_repository_test[i]):
                working = False
        self.assertEqual(True, working)

    def test_phrase_file_service(self):
        phrase_repository = []
        phrase_1 = Phrase.Phrase()
        phrase_1.set_phrase("Marul este delicios")
        phrase_2 = Phrase.Phrase()
        phrase_2.set_phrase("Masina este rapida")
        phrase_repository.append(phrase_1)
        phrase_repository.append(phrase_2)
        self.__pfs.write_phrases(phrase_repository)
        phrase_repository_test = self.__pfs.read_phrases()
        working = True
        if len(phrase_repository) != len(phrase_repository_test):
            working = False
        for i in range(len(phrase_repository)):
            if not phrase_repository[i].__eq__(phrase_repository_test[i]):
                working = False
        self.assertEqual(True, working)
