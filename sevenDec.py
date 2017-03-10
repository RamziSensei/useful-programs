def sevenPostDec(a):
    numDec = str(a/7)
    print(numDec)
    decIndex = numDec[numDec.index(".")+1:]
    decList = []
    for i in decIndex:
        decList.append(int(i))
    print(sum(decList))
        

sevenPostDec(10)
