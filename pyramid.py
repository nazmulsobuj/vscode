row = 5
for i in range(0, row):
    for j in range(0, i):
        print(" ", end=" ")
    k = row
    while k > i:
        print(" * ", end=" ")
        k -= 1
    print()
for i in range(0, row):
    for j in range(row, i+1, -1):
        print(" ", end=" ")