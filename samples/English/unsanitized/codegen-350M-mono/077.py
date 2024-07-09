
def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    '''
    for b in a:
        if b == b**3:
            return True
    return False

test_cases = [
    (1, True),
    (3, False),
    (10, True),
    (0, False),
    (2, True),
    (14, True),
    (32, False)
]

for a, expected in test_cases:
    print(f'{a} = {expected}')
    answer = iscube(a)
    print(f'Expected = {expected}')
    print(f'Comparing answer to number {a} = {answer}')
    assert answer == expected