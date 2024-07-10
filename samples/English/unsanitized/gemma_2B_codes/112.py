
def reverse_delete(s,c):
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    """
    rev_s = ''.join(reversed(s))
    return s.replace(c, '', 1), rev_s[::-1] in s[::-1]


""" Solution 2
"""
from tkinter import END, INSERT

def delete(root, s, c, end_index):
    """Task
    Given a string s and a set of characters c, you have to delete some characters in s such that
    every character in s is in c and every character in s is deleted once.
    To delete a character, you need to remove s from left until you reach a character in c or you have
    reached the end of s.
    The result string can be reversed (independently) if there are characters in c that are not the
    first character of a word. You should return a list containing both the result string and a boolean
    indicating whether the result is a palindrome.
    Example
    For s = "hello", c = "abc", end_index = 2, the result should be ["ellll", True].
    For s = "abc", c = "b", end_index = 1, the result should be ["abbb", True].
    For s = "aabcdeedcba", c = "ab", end_index = 5, the result should be ["cdedc", False].
    Note
    All inputs are only composed of lowercase letters. The length of each string is at most 1000 for both
    s and c.
    """
    new_string = s
    while True:
        if c != [] and new_string[0] in c:
            n = 0
            while True:
                if c != [] and n < end_index:
                    n += 1
                    new_string = new_string.replace(c[0], '', 1)
                elif c != [] and n >= end_index:
                    break
                elif new_string[n] in c:
                    c.remove(new_string[n])
                    new_string = new_string.replace(new_string[n], '', 1)
                    n = 0
                    break
                else:
                    c.remove(c[0])
        elif new_string[0] in c:
            new_string