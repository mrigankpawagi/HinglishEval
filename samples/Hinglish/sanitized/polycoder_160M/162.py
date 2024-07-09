def string_to_md5(text):
    """
    Ek string 'text' di gayi hai, uska md5 hash equivalent string return karo.
    Agar 'text' ek khali string hai, to None return karo.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    text = text and text.encode("utf-8")
    s_dict = dict(hashlib.md5_new(text).hexdigest())
    s_dict[_time] = text
    if len(s_dict) == 0:
        return None

    md5_list = []
    for i in reversed(s_dict.keys()):
        md5_list.append(s_dict[i].replace(lambda l: i.encode("utf8"), ""))
    return md5_list
