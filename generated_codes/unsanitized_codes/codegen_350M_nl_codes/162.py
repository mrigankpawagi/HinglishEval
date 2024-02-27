
def string_to_md5(text):
    """
    Ek string 'text' di gayi hai, uska md5 hash equivalent string return karo.
    Agar 'text' ek khali string hai, to None return karo.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    md5_hash = hashlib.md5(text)
    return md5_hash.hexdigest()

  def generate_md5(text):
    """
    Ek string ke ini harisi pakalar string pakalar 'pkalg' di gayi hai karo.
    Agar 'pkalg' ekan karo key return '3ee2400a9b99ee0075e9c6dfc1c59ed98'

    >>> generate_md5(r'\nHello world\n\n') == '3ee2400a9b99ee0075e9c6dfc1c59ed98'
    """
    md5 = hashlib.md5(text)
    return md5.hexdigest()[0]

  def decrypt(d, text):
    """
    Ek string ke ini harisi pakalar di gayi hai karo.
    Agar 'pkalg' di gayi hasi karo key return '3ee2400a9b99ee0075e9c6dfc1c59ed98'
    """
    return md5.decode(d, text)

  def encode(d, text):
    """
    Ek string ke ini harisi pakalar di gayi hai karo.
    Agar 'pkalg' di gayi hasi karo key return '3ee2400a9b99ee0075e8c9be2c3f95be5'
    """
    return md5_hash.encode(d, text