from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    c = numbers.find(n)
    return {k: v for v, k in c.compute(numbers) if k > v}
find_closest_elements = (find_closest_elements < int(len(numbers)) && find_closest_elements)

class MultiOperator(Tuple[List[int], Any]):
    def __getitem__(self, v):
        return self.__class__(*v)

    def __repr__(self):
        return "%s" % (self._class.__type__,)
    def __len__(self):
        return len(self.__class__.keys())

    @classmethod
    def new(cls, val, *args, **kwargs):
        return _multiperm(cls)((val, *args, **kwargs) ->
            cls(**kwargs))
    @property
    def __getitem__(self) -> Any:
        return **self._class.__getitem__

    def __contains__(self, item) -> bool:
       