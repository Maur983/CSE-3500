def lisnum(a, b):
    print(','.join(str(x) for x in range(a, b+1) if x%5==0 or x%7==0))
lisnum(1,10)