sample = 'how have you been today ?'

L = []

for i in sample.split():
    print(i.capitalize())
    L.append(i.capitalize())

print(" ".join(L))



