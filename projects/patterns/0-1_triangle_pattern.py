n = 4

for i in range(1,n+1):
    for j in range(i): # for starting from 0 -> 1, i+1 & for starting from 1 -> i
        print((i+j)%2,end=" ")
    print()