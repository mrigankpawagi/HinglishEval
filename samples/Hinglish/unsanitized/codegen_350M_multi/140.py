
def fix_spaces(text):
    """
    Diye gaye string text mein, saare spaces ko underscores se replace karo,
    aur agar ek string mein 2 se zyada consecutive spaces ho,
    toh saare consecutive spaces ko - se replace karo.
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    if not text:
        return ""
    orig = text
    for _ in range(5):
        text = re.sub("\s+", " ", text)
    return text.strip()


parser = argparse.ArgumentParser(description='Convert spanish to french, and revert.')
parser.add_argument('file', type=argparse.FileType('r'), help='Name of the file where spanish_srti has been read.')
args = parser.parse_args()
file_data = open(args.file, encoding='utf8').read()
parser.print_help()
file_data = fix_spaces(file_data)

# Replace consecutive spaces
# file = "Example_2"
file = args.file

# Remove consecutive spaces from end of file
# file = "Example_1"
# file = " Example 2"

srtData = file_data.replace("Spanner d'Espagne", "Dj", 1)
srtData = srtData.replace("Spanner d'Espagne", "Dj Dj", 2)
srtData = srtData.replace("Spanner d'Espana", "Dj Dj", 2)
srtData = srtData.replace("Dj Dj", "Dj Dj", 2)

f = open(file, 'w')
f.write(srtData)