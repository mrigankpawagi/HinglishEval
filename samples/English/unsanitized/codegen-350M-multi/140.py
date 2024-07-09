
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
    new_text = ""
    for match in re_match(r"\s*[\w-]+\s*", text):
        new_text += match[1]
    return new_text


if __name__ == '__main__':
    import pprint
    output = input("Output file: ")
    infile = open(output, 'r')
    infile.readline()
    data = json.load(infile)
    pprint.pprint(data,10, indent=4)

    infile.seek(0)
    dict_data = fix_spaces(infile.read())
    pprint.pprint(dict_data)
    infile.close()

    
