import sys
from Controller import Controller


class UI:
    """
    This class contains the UI of the application.
    """

    def __init__(self):
        """
        The default constructor that contains the initialization of the controller.
        """
        self.__validator = Controller.Validator()
        self.__controller = Controller.Controller()

    __menu_variables = "    ~~~Main Menu~~~ \n 1.Generate phrases \n 2.Print percentage of correct phrases \n " \
                       "3.Generate report \n 4.Verify how many phrases have correct topic \n 0.Exit \n"

    def main_menu(self):
        while True:
            print(self.__menu_variables)
            _choice = input("Your choice: ")
            _choice = self.__validator.validate_int(_choice)

            if _choice == 1:
                self.__generate_phrases()
            elif _choice == 2:
                self.__print_percentage()
            elif _choice == 3:
                self.__generate_report()
            elif _choice == 4:
                self.__correct_topic()
            if _choice == 0:
                sys.exit(0)

    def __generate_phrases(self):
        no_of_phrases = input("Number of Phrases: ")
        no_of_phrases = self.__validator.validate_int(no_of_phrases)
        check = self.__controller.generate_phrases(no_of_phrases)
        if check is True:
            for phrase in self.__controller.repo.phrases.get_all():
                print(phrase.get_phrase())
        else:
            print("No words found for the creation of phrases.")

    def __print_percentage(self):
        percentage = self.__controller.get_percentage_of_correct_phrases()
        if percentage is None:
            print("No phrases found.")
        else:
            print(str(percentage), "% phrases are formulated correct(V + S + A)")

    def __generate_report(self):
        check = self.__controller.get_report_of_appearances()
        if check is True:
            print("The report was generated in report.txt file.")
        else:
            print("No words found for the report.")

    def __correct_topic(self):
        no_of_correct_topic_phrases = self.__controller.get_correct_topic_phrases()
        if no_of_correct_topic_phrases is not None:
            print(str(no_of_correct_topic_phrases), " phrases have correct topic (S + V + S +A)")
        else:
            print("No phrases found.")
