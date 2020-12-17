import re
"""
XXXX redacted
"""
def redact(sent, word, case=False, whole=False, overkill=False):
    caseflag =  0 if case else re.I

    def replacer(mo):
        l = mo.end(0) - mo.start(0)
        return 'X' * l

    word0 = word

    if whole:
        word0 = r'\b' + word + r'\b'
    if overkill:
        word0 = r'\b' + r'\w*' + word + r'\w*' + r'\b'
        
    return re.sub(word0, replacer, sent, flags=caseflag)

test = "Toms bottom tomato is in his stomach while playing the 'Tom-tom' brand tom-toms. That's so tom."

print(redact(test, 'Tom', case=True, whole=True))
print(redact(test, 'Tom', whole=True))
print(redact(test, 'Tom', whole=False))
print(redact(test, 'Tom', whole=False, overkill=True))


