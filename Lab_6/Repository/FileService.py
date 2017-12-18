from Domain import Word, Phrase


class WordFileService:
    @staticmethod
    def write_words(word_list, word_type):
        """
        This method will write in file words from a received list.
        :param word_type: Received type of the words.
        :param word_list: Received list to be written in the file.
        """
        try:
            file_name = word_type.name.lower() + "s.txt"
            f = open(file_name, "w")
            for word in word_list:
                f.write(word.get_value() + ", \n")
            f.close()
        except Exception:
            print("Could not save file")

    @staticmethod
    def read_words(word_type):
        """
        This method will read words from file.
        :param word_type: Type of the words that need to be read.
        :return: A list containing words stored in the file.
        """
        word_list = []
        try:
            file_name = word_type.name.lower() + "s.txt"
            f = open(file_name, "r")
            for line in f.readlines():
                split_line = line.split(",")
                word_list.append(Word.Word(split_line[0], word_type))
            f.close()
        except Exception:
            print("Could not read file")
        return word_list


class PhraseFileService:
    @staticmethod
    def write_phrases(phrase_list):
        """
        This method will write in file phrases from a received list.
        :param phrase_list: Received list to be written in the file.
        """
        try:
            f = open("phrases.txt", "w")
            for phrase in phrase_list:
                f.write(phrase.get_phrase() + " \n")
            f.close()
        except Exception:
            print("Could not save file")

    @staticmethod
    def read_phrases():
        """
        This method will read phrases from file.
        :return: A list containing phrases stored in the file.
        """
        phrases_list = []
        try:
            f = open("phrases.txt", "r")
            for line in f.readlines():
                split_line = line.split(".")
                phrase = Phrase.Phrase()
                phrase.set_phrase(split_line[0][0:-2])
                phrases_list.append(phrase)
            f.close()
        except Exception:
            print("Could not read file")
        return phrases_list


class ReportFileService:
    @staticmethod
    def write_reports(report_list):
        """
        This method will write in file reports from a received list.
        :param report_list: Received list to be written in the file.
        """
        try:
            f = open("report.txt", "w")
            for report in report_list:
                f.write(report + " \n")
            f.close()
        except Exception:
            print("Could not save file")
