
def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''
    def is_nested_bracket_subsequence(incoming_nested_string):
        '''Takes the incoming nested string and determines if it is a valid nested subsequence.'''
        
        num_of_square_brackets = 0 #counter for counting how many square brackets found in nested_string

        '''
        Here I check the if there are four in a row
        '''
        '''
        for each time I check that the number of previous square brackets in that subsequence is greater than or equal to the number of next square brackets
        '''
        '''
            For example: 
            incoming_nested_string = [], 1 => True
            incoming_nested_string = [], 2 => False
            incoming_nested_string = [['[]'], 3 => True
            incoming_nested_string = ['[]', '[]', '[]'], 4 => False
            incoming_nested_string = [[], ['[]'], 5 => True
            incoming_nested_string = [[[]], ['[]'], 6 => False
        '''
        for square_bracket in incoming_nested_string:
            if num_of_square_brackets == square_bracket:
                num_of_square_brackets +=1
            elif num_of_square_brackets > square_bracket and num_of_square_brackets <= square_bracket +3:
                num_of_square_brackets = square_bracket +3
            