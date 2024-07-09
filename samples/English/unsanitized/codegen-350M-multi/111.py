
def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """
    def get_count(string):
        return sum(1 for i in range(len(string)-1)) if i == len(string)-1 else 0
    n_letters = len(string)
    repetitions = (repetition for i in range(n_letters) if string[i] == string[i+1]) + [repetition]
    result = {}
    result[repetition[0]] = get_count(string)
    for i in repetitions:
        j = 0
        while j < n_letters - 1:
            j += 1
            if i is repetition[j]:
                result.setdefault(i, 0)
                result[i] = max(result[i], get_count(string))
        result[i] = get_count(string)
    return sum(result[i] for i in repetitions)


class Solution:
    def findRepeatedWords(self, words):
        """
        Time complexity : O(logn)
        Space complexity : O(1)
        
        """
        if not words:
            return list()

        queue = collections.deque()
        max_cnt = 0
        cnt = 0
        for w in words:
            if w and w in queue:
                cnt += 1
                queue.append(w)
            else:
                max_cnt = max(max_cnt, cnt)
                queue.append(w)
        return max_cnt


sol = Solution