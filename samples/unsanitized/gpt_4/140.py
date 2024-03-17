Here is the Python function that fulfills the requirements specified in the docstring:

```python
import re

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
    text = re.sub(' {2,}', '-', text)
    text = text.replace(' ', '_')
    return text
```

This function uses the `re` module to replace all occurrences of two or more consecutive spaces with a hyphen. Then it replaces all remaining spaces with underscores.