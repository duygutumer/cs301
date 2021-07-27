import time
import random

count = 0

def lcs(X,Y,i,j):
    global count
    if (i == 0 or j == 0):
        count += 1
        return 0
    elif X[i-1] == Y[j-1]:
        return 1 + lcs(X,Y,i-1,j-1)
    else:
        return max(lcs(X,Y,i,j-1),lcs(X,Y,i-1,j))

dna = ["c","t","a","g"]

nm = 20

def randomdna(count):
    d = ""
    for i in range(count):
        d += random.choice(dna)
    return d
for i in range(30):
    #X = randomdna(nm)
    #Y = randomdna(nm)
    X = "A"*nm
    Y = "B"*nm
    count = 0
    start = time.time()

    VAL = lcs(X, Y, nm, nm)

    end = time.time()

    #print(VAL)
    print(X, Y)
    print(end - start)
    #print("Passed through the function", count, "times.")
