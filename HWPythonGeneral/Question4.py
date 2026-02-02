def twonum(a,b):
    nli=""
    for i in range(a,b+1):
        if i%5==0 or i%7==0:
            nli+=str(i)+", "
    print(nli[:-2])
twonum(1,10)