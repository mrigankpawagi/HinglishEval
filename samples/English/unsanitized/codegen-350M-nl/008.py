from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    raise NotImplementedError('sum_product must be implemented')

sum_product = sum_product


class NumericType(tuple) with type_ancestor:
    def __new__(cls, kwargs) -> NumericType:
        new = kwargs.pop('_kind', Object)
        new.kwargs['kind'] = new_kind
        kwargs['kwargs.packed'] += ['', '@', '@', '{', '}'.format(kwargs.get, kwargs.get)
        return new


class Numeric(tuple) with type_ancestor:
    def __new__(cls, dtype):
        return IntegerType(type_name=data_type_or_default, dtype=dtype)


## This class extends all three of those, except that it only includes the
## "real" objects, i.e. actual numbers.
##
class RealObject(data_type['realobject'].Mock):
    __slots__ = ['_dtypes',]
    # This is an enum
    Dtypes = (0, int, bool, float, int64, str, real, int8, uint8, uint, real, float, bytearray)


#
# DataType.__slots__: 
#
# This list contains data types whose associated values (including the raw
# values) are stored.
class DataType(data_type['