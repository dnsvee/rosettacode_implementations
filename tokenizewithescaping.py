txt = "one^|uno||three^^^^|four^^^|^cuatro|"
print(txt)

escaped = False
word = []
for c in txt:
    if escaped:
        word.append(c)
        escaped = False
        continue

    if c == '|':
        print(''.join(word))
        word = []
        continue

    if c == "^":
        escaped = True
        continue

    word.append(c)




