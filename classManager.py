#Class List + Total Class List
c7A = ["Alice", "Bob", "Charlie"]
c8B = ["Ryu", "Ken", "Akuma"]
cTest = ["Rob", "Alex", "Ramzi"]
cBestClass = ["Ramzi", "Zoe"]

allClasses = {"7A": c7A, "8B": c8B, "TEST": cTest, "BESTCLASS": cBestClass}


#Booleans + initialisations
validClass = False
runProgram = True
validMainRunInputs = ["1","2","9"]



#Valid class input + Gathering class data
currentClass = input("Select a Class: ").upper()

while validClass == False:

  if currentClass in allClasses:
    print("Found")
    validClass = True
    
  else:
    currentClass = input("\nNot Found, Try again: ").upper()

currentClassList = allClasses[currentClass]


#Functions, lovely Functions
def allMerit(classList):
  allMeritRunner = True
  print("\nALL MERIT MODE ACTIVATED\n")
  classList = currentClassList
  #print(classList)

  namePicker = input("Select a name to remove, 'end' to finish: ")
  
  while allMeritRunner:
    
    if namePicker == "end":
      print("\nFinished! Final Merit list is: ")
      print(classList)
      allMeritRunner = False
      
    elif namePicker not in classList:
      namePicker = input("\nNot found, please try again: ")

    else:
      classList.remove(namePicker)
      print("\n" + namePicker + " has been removed.")
      namePicker = input("\nFound, input another name or 'end': ")
    

  
def gainMerit():
  print("gain merit mode inFunc")


#Begin the main program
print("\nWelcome, " + currentClass + "\n")
print("People in class: ")
print(currentClassList)
print("\n")

while runProgram:

  
  selection = input("What do you want to do? \n1: All Merit Mode \n2: Gain Merit Mode \n9: Quit\n:")

  if selection not in validMainRunInputs:
    selection = input("\nTry again, please input another number: ")
    
  elif selection == "1":
    allMerit(currentClassList)
    exit()
    
  elif selection == "2":
    print("GAIN MODE ACTIVATED")
    gainMerit(currentClassList)
    exit()
    
  elif selection == "9":
    print("bai bai")
    runProgram = False
    
  else:
    print("You should not be here....uh oh")
  
