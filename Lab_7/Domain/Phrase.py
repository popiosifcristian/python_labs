from random import shuffle


class Phrase(object):
    def __init__(self):
        self.__words = []
        self.__phrase = ""

    def __str__(self):
        """
        This method overrides the basic __str__ method and returns a human readable string.
        :return: The string representation of the Phrase class.
        """
        return 'Phrase{Phrase: ' + self.__phrase + '}'

    def __repr__(self):
        """
        This method overrides the basic __repr__ method and returns a human readable string.
        :return: The string representation of the Phrase class.
        """
        return 'Phrase{Phrase: ' + self.__phrase + '}'

    def __attrs(self):
        """
        This method returns the attributes of this instance of Phrase class.
        :return: Value and type of this phrase.
        """
        return self.__words, self.__phrase

    def __eq__(self, other):
        """
        This method overrides the basic __eq__ methods and verify if the received object is equal to this instance
        of Phrase class.
        :param other: Other object to be verified.
        :return: True if the received object is equal with this word, otherwise False.
        """
        return isinstance(other, Phrase) and self.__attrs() == other.__attrs()

    def get_words(self):
        """
        Getter for words propriety.
        :return: The word list of the phrase.
        """
        return self.__words

    def set_words(self, words):
        """
        Setter for words propriety.
        :param words: The new words list to be set.
        """
        self.__words = words

    def get_phrase(self):
        """
        Getter for phrase propriety.
        :return: Phrase of the phrase.
        """
        return self.__phrase

    def set_phrase(self, new_phrase):
        """
        Setter for phrase propriety.
        :param new_phrase: The new phrase to be set.
        """
        self.__phrase = new_phrase

    def add_word(self, word):
        """
        This method will add a word to the word list and will add it to the end of the phrase too.
        :param word: The word to be added.
        """
        if len(self.__words) == 0:
            self.__phrase = self.__phrase + word.get_value().title()
        else:
            self.__phrase = self.__phrase + " " + word.get_value()
        self.__words.append(word)

    def shuffle_phrase(self):
        new_phrase = ""
        shuffle(self.__words)
        for index in range(len(self.__words)):
            if index == 0:
                new_phrase = new_phrase + self.__words[index].get_value().title()
            else:
                new_phrase = new_phrase + " " + self.__words[index].get_value()
        self.__phrase = new_phrase
