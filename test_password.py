import unittest


class TestMakePassword(unittest.TestCase):

    def test_complexity_one(self):
        '''
        Complexity 1: only lowercase chars
        Complexity 2: Previous level plus at least 1 digit
        Complexity 3: Previous levels plus at least 1 uppercase char
        Complexity 4: Previous levels plus at least 1 punctuation char
        '''
        from password import make_password

        assert make_password(7, 1)


class TestCheckPasswordLevel(unittest.TestCase):

    def test_only_lowercase_1(self):
        '''
        Complexity 1: If password has only lowercase chars
        '''
        from password import check_password_level, make_password

        assert check_password_level(make_password(7, 1)) == 1
        assert check_password_level(make_password(8, 1)) != 1
        assert check_password_level(make_password(7, 1) + '123') != 1

    def test_lowercase_digits_2(self):
        '''
        Complexity 2: Previous level condition and at least 1 digit
        '''
        from password import check_password_level, make_password

        assert check_password_level(make_password(7, 2)) == 2
        assert check_password_level(make_password(7, 2) + 'AAA') != 2

    def test_length_8_lowercase_2(self):
        '''
        Complexity 2: password has length >= 8 chars and only lowercase chars
        '''
        from password import check_password_level, make_password

        assert check_password_level(make_password(8, 1)) == 2
        assert check_password_level(make_password(80, 1)) == 2

    def test_lowercase_digits_uppercase_3(self):
        '''
        Complexity 3: Previous levels condition and at least 1 uppercase char
        '''
        from password import check_password_level, make_password

        assert check_password_level(make_password(8, 3)) == 3
        assert check_password_level(make_password(80, 3)) == 3
        assert check_password_level(make_password(8, 3) + '}{') != 3

    def test_length_8_lowercase_digits_3(self):
        '''
        Complexity 3: password has length >= 8 chars and only lowercase and digits
        '''
        from password import check_password_level, make_password

        assert check_password_level(make_password(8, 2)) == 3
        assert check_password_level(make_password(8, 2) + 'AAAAA') == 3

    def test_lowercase_digits_uppercase_punctuation_4(self):
        '''
        Complexity 4: Previous levels condition and at least 1 punctuation
        '''
        from password import check_password_level, make_password

        assert check_password_level(make_password(7, 4)) == 4
        assert check_password_level(make_password(80, 4)) == 4


if __name__ == '__main__':
    unittest.main()
