from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Diye gaye prefix se shuru hone wale strings ke liye input list ko filter karo.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return filter_bys[prefix, '.'].extend(strings).sort_by(None)


class LambdaFunction(object):
    """
    class-transparent lambda function, katko logic style.
    :param func_args: the list of lambda parameter names that are passed to
    the function.
    :param params: the tuple of lambda parameters passed in as argument list.  If
    the default value is `[]`, the entire function will pass all arguments through
    `params` in the lambda function.
    :param default_return: a lambda function that can't be returned by callers
    of this lambda function will be returned: if `func_args` is `None`, the function
    will return `False`.
    """
    def __call__(self, func_args, params):
        """
        called by lambda function with all the parameters and return value
        passed it directly
        :returns: a lambda function object, or `None`
         """
        return self(func_args, params)
        
    def __call__nf(self, func_args, params):
        """
        called by lambda function object or list-with-params
        :returns: a lambda function object or list of function objects for
        the lambda function
 