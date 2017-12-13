class Word(object):
    def __init__(self, value, word_type):
        self.__value = value
        self.__type = word_type

    def __str__(self):
        """
        This method overrides the basic __str__ method and returns a human readable string.
        :return: The string representation of the Word class.
        """
        return 'Word{Value: ' + self.__value + ', Type: ' + self.__type.name + '}'

    def __repr__(self):
        """
        This method overrides the basic __repr__ method and returns a human readable string.
        :return: The string representation of the Word class.
        """
        return 'Word{Value: ' + self.__value + ', Type: ' + self.__type.name + '}'

    def __attrs(self):
        """
        This method returns the attributes of this instance of Word class.
        :return: Value and type of this word.
        """
        return self.__value, self.__type

    def __eq__(self, other):
        """
        This method overrides the basic __eq__ methods and verify if the received object is equal to this instance
        of Phrase class.
        :param other: Other object to be verified.
        :return: True if the received object is equal with this word, otherwise False.
        """
        return isinstance(other, Word) and self.__attrs() == other.__attrs()

    def get_value(self):
        """
        Getter for value propriety.
        :return: The value of the word.
        """
        return self.__value

    def set_value(self, value):
        """
        Setter for the value propriety.
        :param value: The new value to be set.
        """
        self.__value = value

    def get_type(self):
        """
        Getter for the value propriety.
        :return: The type of the word.
        """
        return self.__type

    def set_type(self, new_type):
        """
        Setter for the type value.
        :param new_type: The new type to be set.
        """
        self.__type = new_type

