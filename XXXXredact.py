import re
"""
XXXX_redacted
"""

def redact(sent, word, case=False, whole=False, overkill=False):
    caseflag =  0 if case else re.I
    letter = '[\w\-]'

    word0 = ""

    if whole:
        def replacer(mo):
            if re.fullmatch(mo.group(0), word, caseflag):
                l = mo.end(0) - mo.start(0)
                return 'X' * l
            return mo.group(0)
        return re.sub(r'[\w\-]+', replacer, sent, flags=caseflag)
    else:
        if not overkill:
            def replacer(mo):
                l = mo.end(0) - mo.start(0)
                return 'X' * l
            return re.sub(word, replacer, sent, flags=caseflag)
        else:
            def replacer(mo):
                if re.search(word, mo.group(0), flags=caseflag):
                    l = mo.end(0) - mo.start(0)
                    return 'X' * l
                return mo.group(0)
        return re.sub(r'[\w\-]+', replacer, sent, flags=caseflag)

    raise "Invalid arguments"
        

test = "Tom? Toms bottom tomato is in his stomach while playing the \"Tom-tom\" brand tom-toms. That's so tom."

word = 'Tom'
print('Redact {}:'.format(word))
print('[w|s|n] ', redact(test, word, case=True, whole=True, overkill=False))
print('[w|i|n] ', redact(test, word, case=False, whole=True, overkill=False))
print('[p|s|n] ', redact(test, word, case=True, whole=False, overkill=False))
print('[p|i|n] ', redact(test, word, case=False, whole=False, overkill=False))
print('[p|s|o] ', redact(test, word, case=True, whole=False, overkill=True))
print('[p|i|o] ', redact(test, word, case=False, whole=False, overkill=True))



