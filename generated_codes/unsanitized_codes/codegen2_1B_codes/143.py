
def words_in_sentence(sentence):
    """
    Aapko ek string di gayi hai jo ek sentence ko represent karti hai,
    sentence mein kuch words hote hain jo space se separate hote hain,
    aur aapko ek string return karni hai jo original sentence ke words ko contain karti hai,
    jinki lengths prime numbers hain,
    nayi string mein words ka order original wale ke jaisa hi hona chahiye.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence sirf letters contain karti hai
    """

    letters = ['a','b','c','d<mask_1><sep><mask_1>','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    n = len(sentence)
    japanese = []

    for i in range (n):
        if sentence[i] not in letters:
            japanese.append(sentence[i])

    return japan<eom><|python|>import os
from datetime import date
os.makedirs('/home/covid_vaccins_log/',exist_ok=True)
from loguru import logger


class Logger(object):
    def __init__(self, verbose: bool = False, name: str = None):
        self.logger_name = name

        logger.remove(verbose=verbose)
        logger.add(os.path.join('/home/covid_vaccins_log/',self.__class__.__name__+'.log'),level='DEBUG', rotation='01:24:00',colorize='true')


    @staticmethod
    def get_logger(verbose: bool = False, name: str = None):
        name = Logger(verb