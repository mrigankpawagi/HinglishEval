
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    return hashlib.md5(text.encode('utf-8')).hexdigest()
# Your code goes here!


def md5_message(message):
    """
    Given a string 'message', return its md5 hash equivalent message.
    If 'message' is an empty string, return None.

    >>> md5_message('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    return hashlib.md5(message).hexdigest()
