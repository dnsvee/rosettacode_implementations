import re
def redact(sent,word,case=False,whole=False):
"""
Redact with XXXs rosettacode example!
"""
    word0 = word
    if not case:
        word0 = word.lower()
        
    res=re.split(r'([^\w])', sent)
    pre = []
    for w in res:
        w0 = w.lower() if not case else w
        if whole and (word0 == w):
            pre.append('x'*len(w))
        elif not whole and re.search(word, w):
            pre.append('x'*len(w))
        else:
            pre.append(w)

    return "".join(pre)

test = "Toms bottom tomato is in his stomach while playing the 'Tom-tom' brand tom-toms. That's so tom."

print(redact(test, 'Tom', case=True, whole=True))


