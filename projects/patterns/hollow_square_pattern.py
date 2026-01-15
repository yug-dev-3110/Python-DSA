n=4
for i in range(n):
    for j in range(n):
        if i == 0 or i == 3 or j == 0 or j == 3:
            print("*", end="")
        else:
            print(" ", end="")
    print()
