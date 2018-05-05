import random
from string import ascii_lowercase as lowercase
from string import ascii_uppercase as uppercase
from string import digits
from string import punctuation


def make_password(length:int, complexity:int) -> str:
    '''Generate a random password with given length

    Allowed complexity levels:
        Complexity 1: only lowercase chars
        Complexity 2: Previous level plus at least 1 digit
        Complexity 3: Previous levels plus at least 1 uppercase char
        Complexity 4: Previous levels plus at least 1 punctuation char

    :param length: number of characters
    :param complexity: complexity level
    :returns: generated password
    '''
    pass


def check_password_level(password: str) -> int:
    '''Return the password complexity level

    Result levels:
        Complexity 1: If password has only lowercase chars
        Complexity 2: Previous level condition and at least 1 digit
        Complexity 3: Previous levels condition and at least 1 uppercase char
        Complexity 4: Previous levels condition and at least 1 punctuation

    Level exceptions:
        Complexity 2: password has length >= 8 chars and only lowercase chars
        Complexity 3: password has length >= 8 chars and only lowercase and digits

    :param password: password
    :returns: complexity level
    '''
    pass
