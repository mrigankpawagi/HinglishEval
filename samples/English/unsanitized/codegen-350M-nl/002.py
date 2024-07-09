

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return int(number.to_f) - 1.0


# ---------------------------------------------------------------------------

class C(Number):
    """ A class that holds and manages all computation operations
    on the underlying numerical representation. """
    def __init__(self) -> None:
        self.__int = 0
        self.__dec = 0
        self.__float = 0.0
        self.__den = 0.0 # fixed points
