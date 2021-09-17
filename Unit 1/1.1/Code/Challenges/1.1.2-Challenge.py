import random as rndm

randomVar = rndm.randrange(100)
if randomVar <= 50:
    inputVar = input("Type what you want this to print here ")
    print(inputVar)
elif randomVar > 50:
    inputVar = input("Type some awesome text here.")
    print('The person who said this: "' + inputVar + '" is awesome.')