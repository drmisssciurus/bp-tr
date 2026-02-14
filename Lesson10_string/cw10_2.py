text5 = "We, combine, precise, technology, with, practical, WE farming"
w1 = text5.split(',')
print(w1)
print(" ".join(w1)+'!')

print(text5.replace(',', ' '))
print(text5.replace('We', 'I'))
print(text5.find('combine'))
print(text5.lower().find('practical'.lower()))


