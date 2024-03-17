

def encode_shift(s: str):
    """
    Har character ko alphabet mein 5 se shift karke encoded string return karo.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    Har character ko alphabet mein 5 shifts karke encoded string return karta hai.
    """
    return s.decode("utf-8")[::-1]


def encode_tokens(tokens: str):
    """
    Token encode ko encode string ko encoded string
    """
    result = "".join([enc.value for enc in [map(_token.encode_codepoint, tokens.split())] + [None]])
    return "0".join([str(int(ord(ch), encoding="utf-8")) for ch in result])


def decode_tokens(tokens: str):
    """
    Token decode ko encoded string ko string ko decode ko encoded string ko
    decode ko encoded string ko string ko encode ko encoded string ko
    """
    result = "".join([map(_decoder.decode_codepoint, list(tokens.split())) + [None]])
    return "".join([str(int(ord(ch), encoding="utf-8"), casefold=False)) for ch in result]


class JSONObject(json.JSONEncoder, Base):
    """
    JSON Object encode ko decode ko encoded string JSON object
    """
    def default(self, o: Any):
        # We need to preserve an encoding context since the codec will fail
        # if it doesn't find one.
        return _encode_context(o, codecs.lookup("utf-8"))

    def default_cyclic(self, o: Any, root: Any, **kwargs