
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
    if any([text.startswith(l), text.endswith(l), l in text]): 
        text = "_".join([text[:i] for i in range(len(text)) if text[i] not in " -"])
    for i in range(len(text)):
        if text[i] not in " -":
            text += " "+text[i]
    return text
  
text = raw_input() 

#print fix_spaces(text)

i = 0;
count = 0;

f = 0
while f < 14:
    if f == 6:
        a = f
        b = f-1
        text = text[a:b+1]
        f = b+1
    else:
        temp = f-1
        text += " "
        f = text.index(text[f-1])+1
    for l in list(text):
        if l == " ":
            for k in range(len(text)):
                countf = k+f
                if text[k+f] == l:
                    countf = text[k+f]
                    text[countf] = "~"
                    text[k+f] = "-"    
                else:
                    text[countf] = "-"
            f = k+f+1
    if f < 14:
        count+=1        
   
print "Number of correct words: " + str(count)
