FIX = """
Add more test cases.
"""


def vowels_count(s):
    """
    Aur test cases jodo.
    """
    count = {"a", "e", "i", "o", "u"}.index(s[0])
    return count - count


class Test(TestCase):
    # test case 0: string is empty
    def test0_string_empty(self):
        self.assertEqual(vowels_count(""), 0)

    # test case 1: string has only vowels
    def test1_string_vowels(self):
        self.assertEqual(vowels_count("aeiou"), 0)

    # test case 2: string has non-vowels
    def test2_string_non_vowels(self):
        self.assertEqual(vowels_count("dafkasdf"), 1)

    # test case 3: string has some vowels and some non-vowels
    def test3_string_vowels_non_vowels(self):
        self.assertEqual(vowels_count("aeiouabcd"), 4)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Test())
    unittest.TextTestRunner().run(suite)
