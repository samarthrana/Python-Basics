#Break statement : terminates loop at a condition

for i in range (1,11):
    if i == 5:
        break
    print(i)

#Continue statement: skips code after continue for that particaular iteration or condition

for i in range(1,11):
    if i == 5:
        continue
    print(i, "hello")

#Pass statement: skips the loop, avoids error messages
for i in range(1,11):
    pass

