from Domain.WordType import WordType
from Repository import AbstractRepository, FileService


class Repositories:
    def __init__(self):
        self.words = AbstractRepository.AbstractRepository()
        self.phrases = AbstractRepository.AbstractRepository()
        self.__initialize_repositories()

    def __initialize_repositories(self):
        noun_list = FileService.WordFileService.read_words(WordType.NOUN)
        for word in noun_list:
            self.words.add(word)
        verb_list = FileService.WordFileService.read_words(WordType.VERB)
        for word in verb_list:
            self.words.add(word)
        adjective_list = FileService.WordFileService.read_words(WordType.ADJECTIVE)
        for word in adjective_list:
            self.words.add(word)


