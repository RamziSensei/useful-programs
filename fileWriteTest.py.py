a = [1,2,3,4]
aList = "".join(str(a))
print(aList)


testFile = open("HEYYYY.txt", "w")
testFile.write(aList)
testFile.close()
