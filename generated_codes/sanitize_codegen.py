def sanitize1(completion, prompt):
    generated = completion[len(prompt):]
    lines = generated.split("\n")
    final_lines = ["\n"]
    for line in lines:
        if line.strip() and line[0].strip():
            break
        final_lines.append(line)
    return prompt + "\n".join(final_lines)

completion= """
def strlen(string: str) -> int:
    \"\"\"
    Diye gaye string ki length return karo
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    \"\"\"
    return len(string)

# print statement will print the output to the actual terminal the python console
# in for some reason even if I run it from command prompt
print "Hello World!!!"

A:

Why not use strcat()?

A:

use len here. Don't use index:
print(len("hello world"))
>>> 11
"""
prompt= "\n\ndef strlen(string: str) -> int:\n    \"\"\"\n    Diye gaye string ki length return karo\n    >>> strlen('')\n    0\n    >>> strlen('abc')\n    3\n    \"\"\""
print(sanitize1(completion, prompt))