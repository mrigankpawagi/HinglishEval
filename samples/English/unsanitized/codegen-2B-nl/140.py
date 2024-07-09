
def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    result = text.split()
    res = []
    for item in result:
        i = 0
        while (i < len(item)) and (item[i] == " "):
            result[i] = "_"+item[i]
            i += 1
        while (i < len(item)) and (item[i] == "- "):
            result[i] = result[i-1]
            i += 1
        result.extend(result[0:i])            
    return "".join(result)            

print fix_spaces('This is a test')

A:

If you are simply going to count the number of characters in the middle of the string, then you can write:
inverted_dic = {}

for k,v in reversed(dic.items()):
    if v[:3] not in inverted_dic:
        inverted_dic[v[:3]] = v

for k,v in reversed(dic.items()):
    if 3*v in dic:
        dic[3*v] = inverted_dic[v