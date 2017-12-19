from Domain.Phrase import Phrase
from Repository import InMemoryRepository, FileService
from random import randint

from Repository import AbstractRepository
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

    @staticmethod
    def check_similarity(phrase, magic_phrase):
        """
        This method will check if received phrase is similar with received magic phrase.
        For this it will check all the words with their values from the same index.
        :param phrase: Received phrase to be checked.
        :param magic_phrase: Received magic phrase for the check.
        :return: True if the phrases are similar, otherwise false.
        """
        for index in range(len(phrase.get_words())):
            if phrase.get_words()[index].get_value() != magic_phrase.get_words()[index].get_value():
                return False
        return True

    @staticmethod
    def get_similarity_report(phrase, magic_phrase):
        """
        This method will return the similarity report dictionary.
        Will check the percentage of similarity and the similar words count.
        :param phrase: Received phrase to be checked.
        :param magic_phrase: Received magic phrase for the similarity report.
        :return: A dictionary that contains the phrase, the magic phrase, the percentage and the similarity words count.
        """
        similarity_count = 0
        for word in phrase.get_words():
            for magic_word in magic_phrase.get_words():
                if word.get_value() == magic_word.get_value():
                    similarity_count += 1
        percentage = int(100 * float(similarity_count) / float(len(phrase.get_words())))
        similarity_dictionary = {'phrase': phrase, 'magic_phrase': magic_phrase, 'percentage': percentage,
                                 'similar_words': similarity_count}
        return similarity_dictionary

    def calculate_similarity_reports(self):
        """
        This method will calculate the similarity report for every phrase from the repo with every magic phrase from
        the repo.
        :return: A list of report dictionaries that have percentage of similarity higher than 0.
        """
        similarity_reports = []
        magic_phrases = self.repo.magic_phrases.get_all()
        phrases = self.repo.phrases.get_all()
        for magic_phrase in magic_phrases:
            for phrase in phrases:
                if len(phrase.get_words()) == len(magic_phrase.get_words()):
                    if not self.check_similarity(phrase, magic_phrase):
                        similarity_report = self.get_similarity_report(phrase, magic_phrase)
                        if similarity_report['percentage'] != 0:
                            similarity_reports.append(similarity_report)
        return similarity_reports

    def get_similar_phrases(self):
        """
        This method will get all phrases that are similar to a magic phrase.
        :return: A dictionary that contains the phrase and the line from the file.
        """
        similar_phrases = []
        magic_phrases = self.repo.magic_phrases.get_all()
        phrases = self.repo.phrases.get_all()
        for magic_phrase_index in range(len(magic_phrases)):
            for phrase_index in range(len(phrases)):
                if len(phrases[phrase_index].get_words()) == len(magic_phrases[magic_phrase_index].get_words()):
                    if self.check_similarity(phrases[phrase_index], magic_phrases[magic_phrase_index]):
                        line = phrase_index + 1
                        similar_phrases.append({'phrase': phrases[phrase_index], 'line': line})
        return similar_phrases

    def update_magic_phrases(self):
        """
        This method will update the in memory magic phrase repository from the magic_phrase.txt
        """
        self.repo.magic_phrases = AbstractRepository.AbstractRepository()
        magic_phrases = FileService.MagicPhrasesFileService.read_phrases()
        for magic_phrase in magic_phrases:
            self.repo.magic_phrases.add(magic_phrase)
        print("In Memory magic phrase repository updated from the magic_phrase.txt file.")


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
