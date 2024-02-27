from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Diye gaye numbers ki list (kam se kam do elements ki) par ek linear transform apply karo,
    aisa ki sabse chota number 0 ban jaye aur sabse bada number 1 ban jaye
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    for i in range(len(numbers) - 1):
        numbers[i] = numbers[i] / float(numbers[i] - numbers[i + 1])
    return numbers
<|python|>

    def __str__(self):
        return '{0} -> ({1}_{2})'.format(self.sig_name, self.parameterized, self.sig_params)


@pytest.mark.parametrize('sig_name,parameterized,sig_param_type', [
    ('cg', ['1', '1_5'],'matrix'),
    ('sig_2', ['a', '2'], 'array'),
    ('sig_2_2', ['a', '3'], 'array'),
    ('sig_1_1', ['1', '1_5'], 'array'),
    ('mat_2:symmetric', ['a', '1'], 'complex'),
    ('mat_3', ['5.0', '7.0'], 'csc'),
    ('mat_complex_4:nontr1', ['t', '3.0_5.0'], 'complex'),
    ('mat_4', ['3.5', '7.5'], 'hermite'),
    ('mat_4_2:symmetric', ['q', '3.5'], 'complex')
])
