
def string_to_md5(text):
    """
    Ek string 'text' di gayi hai, uska md5 hash equivalent string return karo.
    Agar 'text' ek khali string hai, to None return karo.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

    # TODO: Convert to base64 - https://www.digitalocean.com/community/tutorials/how-to-use-base64-encoding-to-convert-an-md5-from-a-string-to-an-md5-hash-in-python
    # ek. tok '\x3e' di hai iha.
    return md5.new(text.encode_utf8().lower()).hexdigest()


