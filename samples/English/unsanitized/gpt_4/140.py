def fix_spaces(text):
    while '  ' in text:
        text = text.replace('  ', ' ')
    text = text.replace(' ', '_')
    text = text.replace('__', '-')
    return text