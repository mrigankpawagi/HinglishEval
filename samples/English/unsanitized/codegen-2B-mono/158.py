
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb","cc"]) == ""aaaaaaa"
    """
    max_str = ""
    for word in words:
        if len(max_str) < len(word):
            max_str = word
        d = get_char_number(word)
        if(max_str == word):
            key = []
            for k,v in d.items():
                if k == "count":
                    d["count"] = v
                if len(d) == 3:
                    return min(max_str)
                key.append(k)
            list_to_append = []
            for i in sorted([str(x) for x in key]):
                list_to_append.append(d[i])
            list_to_append.reverse()
            list_to_append.reverse()
            d = dict({})
            d["count"] = list_to_append[0]
            for i in range(1, len(list_to_append)):
                if d.get('count') > list_to_append[i]:
                    d['count'] = list_to_append[i]
            d = dict(sorted(d.items(),reverse=True))
            
            print(max_str + str(d.values()))
            d["count"] = d.items()[0][1]
        else:
            d = get_char_number(word)
            if d.get("count") >= max_str.get("count"):
                if key:
                    del d["count"]
                    del d["characters"]
                else:
                    d["count"] = d["count"] + max_str.get("count")
