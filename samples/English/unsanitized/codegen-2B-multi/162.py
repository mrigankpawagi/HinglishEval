
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text: return None
    if sys.version_info >= (2, 4, 0):
        return hashlib.md5(text).hexdigest()
    else:
        import md5
        return md5.new(text).hexdigest()

