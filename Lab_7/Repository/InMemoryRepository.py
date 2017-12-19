from Domain.WordType import WordType
from Repository import AbstractRepository, FileService


class Repositories:
    def __init__(self):
        self.nouns = AbstractRepository.AbstractRepository()
        self.adjectives = AbstractRepository.AbstractRepository()
        self.verbs = AbstractRepository.AbstractRepository()
        self.phrases = AbstractRepository.AbstractRepository()
        self.magic_phrases = AbstractRepository.AbstractRepository()
        self.__initialize_repositories()

    def __initialize_repositories(self):
        noun_list = FileService.WordFileService.read_words(WordType.NOUN)
        for word in noun_list:
            self.nouns.add(word)
        verb_list = FileService.WordFileService.read_words(WordType.VERB)
        for word in verb_list:
            self.verbs.add(word)
        adjective_list = FileService.WordFileService.read_words(WordType.ADJECTIVE)
        for word in adjective_list:
            self.adjectives.add(word)
        magic_phrases = FileService.MagicPhrasesFileService.read_phrases()
        for magic_phrase in magic_phrases:
            self.magic_phrases.add(magic_phrase)
