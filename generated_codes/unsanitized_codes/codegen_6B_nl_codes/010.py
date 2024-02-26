

def is_palindrome(string: str) -> bool:
    """ Test karo ki kya diya gaya string palindrome hai ki nahi """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """
    Diye gaye string ko check karo ki woh palindrome hai ya nahi.
    """
    if is_palindrome(string):
        return string[::-1][::-1]
    else:
        return string.lower()


def main() -> None:
    while True:
        try:
            print('Enter a string: ', end='')

            string = input()
            if string!= '':
                print('Input accepted.')
            else:
                print('Aborting.')
                break

            str = make_palindrome(string)
            print('Original string -->'+ string)
            print('\n'
                  'Palindrome string -->'+ str
                  '\n' + str)
            if string == str:
                print('')
                if str == str[::-1]:
                    print('Palindrome')