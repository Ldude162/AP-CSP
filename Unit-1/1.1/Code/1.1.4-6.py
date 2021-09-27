'''
Made by Linus Reynolds
On 9/23/2021
1.1.4 #6
'''
breakLoop = True

while(breakLoop):
    num1 = int(input("Please type in a number "))
    num2 = int(input("Type in another one. "))

    if num1 % num2 == 0:
        print("They are divisible!")
        breakLoop = False
    else:
        print("These numbers are not divisible! Try again!")