def printpatten(n):
    r = n // 2
    count = r

    for i in range(r):
        for j in range(r,i,-1):
            if j != r:
                print(" * "+str(count),end=" ")
            else:
                print(count, end=" ")

        count -=1
        print()

    count += 1
    for i in range(r):
        for j in range(i+1):
            if j != 0:
                print(" * "+str(count),end="  ")
            else:
                print(count,end=" ")
                
        count +=1
        print()


printpatten(8)