
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
    text = text.replace("\n", "")
    return space_re.sub("_", text).replace("   ", "_")

if __name__ == '__main__':
    file_count = 0
    with codecs.open(sys.argv[1], encoding='utf-8') as file_in:
        with codecs.open(sys.argv[2], 'w', encoding='utf-8') as file_out:
            for line in file_in:
                file_count += 1
                lines = line.split('\n')
                for item in lines:
                    tokens = tokenize(fix_spaces(item))
                    for token in tokens:
                        file_out.write(token)
                if lines[0]!= lines[-1]:
                    file_out.write("\n")
    print("Saved: ", file_count, " files")