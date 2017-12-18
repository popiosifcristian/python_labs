from Domain.Phrase import Phrase
from Repository import InMemoryRepository, FileService
from random import randint

from Repository.FileService import PhraseFileService


class Controller:
    def __init__(self):
        self.repo = InMemoryRepository.Repositories()

    def generate_phrases(self, no_of_phrases):
        """
        This method generates a specific no of phrases from the received number.
        :param no_of_phrases: Specific no of phrases.
        :return: True if there are more than 4 words to generate the phrase otherwise False.
        """
        nouns = self.repo.nouns.get_all()
        verbs = self.repo.verbs.get_all()
        adjectives = self.repo.adjectives.get_all()
        if len(nouns) > 0 and len(verbs) > 0 and len(adjectives) > 0:
            for index in range(no_of_phrases):
                phrase = Phrase()

                random_nouns_index = randint(0, len(nouns) - 1)
                random_verbs_index = randint(0, len(verbs) - 1)
                random_adjectives_index = randint(0, len(adjectives) - 1)
                random_noun = nouns[random_nouns_index]
                random_verb = verbs[random_verbs_index]
                random_adjective = adjectives[random_adjectives_index]
                phrase.add_word(random_noun)
                phrase.add_word(random_verb)
                phrase.add_word(random_adjective)

                random_no_of_words = randint(0, 2)
                if random_no_of_words > 0:
                    for random_word_index in range(random_no_of_words):
                        random_word_type = randint(1, 3)
                        if random_word_type == 1:
                            random_nouns_index = randint(0, len(nouns) - 1)
                            random_noun = nouns[random_nouns_index]
                            phrase.add_word(random_noun)
                        elif random_word_type == 2:
                            random_verbs_index = randint(0, len(verbs) - 1)
                            random_verb = verbs[random_verbs_index]
                            phrase.add_word(random_verb)
                        else:
                            random_adjectives_index = randint(0, len(adjectives) - 1)
                            random_adjective = adjectives[random_adjectives_index]
                            phrase.add_word(random_adjective)
                phrase.shuffle_phrase()
                self.repo.phrases.add(phrase)

            PhraseFileService.write_phrases(self.repo.phrases.get_all())
            return True
        else:
            return False

    def get_correct_phrases(self):
        """
        This method will return None if in the repository is no phrase, otherwise all the correct phrases (V + S + A)
        :return: All the correct phrases with the specific propriety of a "correct phrase".
        """
        correct_phrases = []
        if len(self.repo.phrases.get_all()) > 0:
            for phrase in self.repo.phrases.get_all():
                if phrase.get_words()[0].get_type().value == "V" and phrase.get_words()[1].get_type().value \
                        == "S" and phrase.get_words()[2].get_type().value == "A":
                    correct_phrases.append(phrase)
            return correct_phrases
        else:
            return None

    def get_percentage_of_correct_phrases(self):
        """
        This method will return the percentage of the correct phrases.
        :return: The percentage of the correct phrases.
        """
        correct_phrases = self.get_correct_phrases()
        if correct_phrases is not None:
            return int(100 * float(len(correct_phrases)) / float(len(self.repo.phrases.get_all())))
        else:
            return None

    @staticmethod
    def word_in_list(specific_word, word_list):
        """
        This method will return the no of appearances of a specific word by value in a word list.
        :param specific_word: The word for the search.
        :param word_list: The specific word list for the search.
        :return: No of appearances of that specific word in the received word list.
        """
        no_of_appearances = 0
        for word in word_list:
            if word.get_value() == specific_word:
                no_of_appearances += 1
        return no_of_appearances

    def get_report_of_appearances(self):
        """
        This method will generate a report of usage for all words stored in the repository and will write the report in
        a specific file.
        :return: True if there is any word stored, otherwise False.
        """
        report_list = []

        if len(self.repo.nouns.get_all()) > 0:
            for word in self.repo.nouns.get_all():
                no_of_appearances = 0
                for phrase in self.repo.phrases.get_all():
                    no_of_appearances += self.word_in_list(word.get_value(), phrase.get_words())
                appearance_word_report = word.get_value() + " - " + str(
                    no_of_appearances) + " appearances - " + word.get_type().value + ";"
                report_list.append(appearance_word_report)

        if len(self.repo.verbs.get_all()) > 0:
            for word in self.repo.verbs.get_all():
                no_of_appearances = 0
                for phrase in self.repo.phrases.get_all():
                    no_of_appearances += self.word_in_list(word.get_value(), phrase.get_words())
                appearance_word_report = word.get_value() + " - " + str(
                    no_of_appearances) + " appearances - " + word.get_type().value + ";"
                report_list.append(appearance_word_report)

        if len(self.repo.adjectives.get_all()) > 0:
            for word in self.repo.adjectives.get_all():
                no_of_appearances = 0
                for phrase in self.repo.phrases.get_all():
                    no_of_appearances += self.word_in_list(word.get_value(), phrase.get_words())
                appearance_word_report = word.get_value() + " - " + str(
                    no_of_appearances) + " appearances - " + word.get_type().value + ";"
                report_list.append(appearance_word_report)

            FileService.ReportFileService.write_reports(report_list)
            return True
        else:
            return False

    def get_correct_topic_phrases(self):
        """
        This method will get the correct topic phases stored (S + V + S + A).
        :return: None if there is no phrase stored in the repository, otherwise the length of the list that contains all
        the phases with the correct topic.
        """
        correct_topic_phrases = []
        if len(self.repo.phrases.get_all()) > 0:
            for phrase in self.repo.phrases.get_all():
                if phrase.get_words()[0].get_type().value == "S" and phrase.get_words()[1].get_type().value == "V" \
                        and phrase.get_words()[2].get_type().value == "S" and \
                        phrase.get_words()[3].get_type().value == "A":
                    correct_topic_phrases.append(phrase)
            return len(correct_topic_phrases)
        else:
            return None


class Validator(object):
    """
    This class contains all the validations for the UI layer of the application.
    """

    @staticmethod
    def check_int(number):
        """
        This method checks if the received string is a digit.
        :param number: The string to be checked
        :return: True if the received string is a digit, otherwise False.
        """
        if number.isdigit() is False:
            return False
        return True

    def validate_int(self, number):
        """
        This methods checks if the received string is an int, if its not it will continuous ask for an int.
        :param number: The received string to be checked.
        :return: Received string converted to int.
        """
        while self.check_int(number) is False:
            number = input("Please enter an digit: ")
        return int(number)
