
def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    
    count = 0

    for index, char in enumerate(S):
        if S[index] in ["!" ,"?", "."]:
            char = str(char).lower()

        if char == "i":
            count += 1
        
    return count




# test cases

if __name__ == '__main__':
    print(is_bored("Hello world"))
    print(is_bored("The sky is blue. The sun is shining. I love this weather"))
    print(is_bored("I can run faster! Can you run as fast as me?!"))
