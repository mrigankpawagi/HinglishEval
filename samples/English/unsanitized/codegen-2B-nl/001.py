from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # https://en.wikipedia.org/wiki/Parenthesis_(mathematics)
    # https://en.wikipedia.org/wiki/Curly_brace

    # https://www.numsa.gov.au/documents/guidelines/ch3_4_8.pdf
    # The definition from this PDF is the following:
    #             A Paren is a Sequence (Group) of parenthesis characters enclosed between
    #             Quotation Marks.
    #             A Paren Group is a Sequence of Parens in which each of the Parens is
    #             neither (a) surrounded by Quotation Marks, nor contained in Quotation Marks.
    #             Each Paren Group that is the last in a Paragraph is (a) surrounded by a Parenthesis, a Paragraph has any number of Paragraphs, a Paragraph may not contain another Paren Group inside a Paragraph, and a Paren should not be surrounded by Quotation Marks.
    #

    def is_parenthesis_in_paren_array(start_pos: int, end_pos: int) -> bool:
        """

        :param start_pos: Position of the start of the first Paren in the group.
        :param end_pos: