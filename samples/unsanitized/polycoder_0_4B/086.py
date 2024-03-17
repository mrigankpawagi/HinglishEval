
def anti_shuffle(s):
    """
    Ek function likho jo ek string leta hai aur uska ordered version return karta hai.
    Ordered version of string, woh string hoti hai jahan saare words (space se separated)
    ko ek naye word se replace kiya jata hai jahan saare characters ko 
    unke ascii value ke basis pe ascending order mein arrange kiya jata hai.
    Dhyan do: Aapko words aur blank spaces ki order sentence mein maintain karni chahiye.

    Jaise ki:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """    if PY2 and s.startswith('\x00-\x2F\x3F...'):
        return s
    if PY2 and s.endswith('\x00-\x2F'):
        return s[:-1]
    if s.startswith(''):
        return ''
    s = s.replace("\t", " ").replace("\n", " ").replace("\"" + ', " ')
    #print s
    s = s.replace("'", "\"") if s.startswith("&quot;") else s
    #print s.replace("\'", '"') # 用来加/减掉"”
    #print '\x00'.join([ c for c in s.split("\x00") if c.isalnum() ])
    #print '\x00'.join([ x for x in s.split("\x00") if x.isdigit() ])
    s = "".join([ s.replace("\"", "\\")  for w in s.split("%") ])
    return s.replace("<", "").replace(">", "")

