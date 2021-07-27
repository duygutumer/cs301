import time
import random

count = 0

def lcs(X,Y,i,j):
    if c[i][j] >= 0:
        return c[i][j]
    if (i == 0 or j == 0):
        c[i][j] = 0
    elif X[i-1] == Y[j-1]:
        c[i][j] = 1 + lcs(X,Y,i-1,j-1)
    else:
        c[i][j] = max(lcs(X,Y,i,j-1),lcs(X,Y,i-1,j))
    return c[i][j]

dna = ["c","t","a","g"]

nm = 5

def randomdna(count):
    d = ""
    for i in range(count):
        d += random.choice(dna)
    return d
for i in range(30):
    #X = randomdna(nm)
    #Y = randomdna(nm)
    count = 0
    X = "A"*nm
    Y = "B"*nm
    c = [[-1 for k in range(6)] for l in range (6)]
    start = time.time()

    VAL = lcs(X, Y, nm, nm)

    end = time.time()

    #print(VAL)
    #print(X, Y)
    print(end - start)
    #print("Passed through the function", count, "times.")
