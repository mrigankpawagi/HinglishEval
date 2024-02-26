def sanitize1(completion, entry_point):
    anchor=completion.find(f"def {entry_point}")
    x=completion.find("\n",anchor)
    generated = completion[x:]
    lines = generated.split("\n")
    final_lines = []
    for line in lines:
        if line.strip() and line[0].strip():
            break
        final_lines.append(line)
    return completion[:x+1] + "\n".join([x for x in final_lines if x.strip()])

def sanitize2(completion, prompt):
    ind=completion.find("```python")
    completion=completion[ind+9:]
    return sanitize1(completion,entry_point="get_closest_vowel")

completion="""
```python
def get_closest_vowel(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    word = word.lower()
    for i in range(1, len(word)-1):
        if word[i] not in vowels and word[i-1] in vowels and word[i+1] in vowels:
            return word[i]
    return ""
```
"""
prompt="\ndef get_closest_vowel(word):\n    \"\"\"\n    Aapko ek word diya gaya hai. Aapka task hai right side se dekhte hue us vowel ko dhundna hai jo \n    do consonants ke beech mein hai (case sensitive).\n    \n    Shuruat aur ending mein jo vowels hain unka count nahi hoga. Agar aapko koi bhi vowel upar diye gaye \n    condition ke hisaab se nahi mila toh khali string return karo. \n\n    Aap maan sakte ho ki diya gaya string sirf English letters se bana hua hai.\n\n    Udaharan:\n    get_closest_vowel(\"yogurt\") ==> \"u\"\n    get_closest_vowel(\"FULL\") ==> \"U\"\n    get_closest_vowel(\"quick\") ==> \"\"\n    get_closest_vowel(\"ab\") ==> \"\"\n    \"\"\""
#prompt="\ndef histogram(test):\n    \"\"\"\n    Ek string di gayi hai jo space separated lowercase letters ko represent karti hai, return karo ek dictionary\n    jisme sabse zyada repeat hone wale letter aur unke corresponding count ho.\n    Agar kai letters ka occurrence same hai, to un sabhi ko return karo.\n    \n    Udaharan:\n    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}\n    histogram('a b b a') == {'a': 2, 'b': 2}\n    histogram('a b c a b') == {'a': 2, 'b': 2}\n    histogram('b b b b a') == {'b': 4}\n    histogram('') == {}\n    \"\"\""

print(sanitize2(completion, prompt))
