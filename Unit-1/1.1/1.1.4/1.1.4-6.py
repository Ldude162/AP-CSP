'''
Made by Linus Reynolds
On 9/23/2021
1.1.4 #6
'''

num1 = int(input("Please type in a number "))
num2 = int(input("Type in another one. "))
while(num1 % num2 != 0):
    print("These numbers are not divisble! Please try again!")
    num1 = int(input("Please type in a number "))
    num2 = int(input("Type in another one. "))
print("They are divisible!")


    