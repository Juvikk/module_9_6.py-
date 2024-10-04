def all_variants(text):
    x = 0
    y = 0
    for x in range(Len(text)):
        for y in range(x + 1, ((lentext) + 1)):
            yield text[x:y]

a = all_variants("abc")
for i in a:
    print(i)
