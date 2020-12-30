"""
tokenize a string with escaping
"""

txt = "one^|uno||three^^^^|four^^^|^cuatro|"

def splitter(txt,sep,esc):
    escaped = False
    word = []
    res = []
    for c in txt:
        if escaped:
            word.append(c)
            escaped = False
            continue

        if c == sep:
            res.append(''.join(word))
            word = []
            continue

        if c == esc:
            escaped = True
            continue

        word.append(c)
    res.append(''.join(word))
    return res

print(splitter(txt,'|','^'))




