import os

cont = True

def openList(list):
    f = open(list + '.txt', 'r')
    print("Here is the elements in the list " + list + ":")
    print(f.read())
    f.close()
    add = 'y'
    while add == 'y':
        add = input("Do you want to add something to the list? (y/n) ")
        if add == "y":
            item = input("What do you want to add? ")
            f = open(list + '.txt', 'a')
            f.write(item + "\n")
            f.close()
            print("Item added!")
    delete = 'y'
    while delete == 'y':
        delete = input("Do you want to delete something from the list? (y/n) ")
        if delete == "y":
            item = input("Which item do you want to delete? Enter the item exactly as it is in the list. ")
            f = open(list + '.txt', 'r')
            lines = f.readlines()
            f.close()
            f = open(list + '.txt', 'w')
            for line in lines:
                if line != item + '\n':
                    f.write(line)
            f.close()
            print("Your list now looks like this:")
            f = open(list + '.txt', 'r')
            print(f.read())
            f.close()


while cont:
    option = input("What would you like to do? (n for new list, v for view, add to, or remove things from an existing list, d to delete a list, or type e to exit the program. ")
    if option == "n":
        name = input("What do you want to name the new list? ")
        if os.path.exists(name + '.txt'):
            print("That list already exists.")
            continue
        else:
            f = open(name + '.txt', 'x')
            f.close()
            add = input("List " + name + " created. What is the first thing you want to add to the list? ")
            f = open(name + '.txt', 'a')
            f.write(add + '\n')
            f.close()
    elif option == "v":
        print("Current lists:")
        for files in os.listdir():
            if files.endswith('.txt'):
                files = files.split('.txt')
                print(files[0])
        list = input("Which list would you like to view? ")
        if os.path.exists(list + '.txt'): 
            openList(list)        
    elif option == 'd':
        print("Current lists:")
        for files in os.listdir():
            if files.endswith('.txt'):
                files = files.split('.txt')
                print(files[0])
        list = input("Which list would you like to delete? ")
        if os.path.exists(list + '.txt'):
            os.remove(list + '.txt')
            print("List " + list + " deleted.")
    elif option == 'e':
        cont = False
    else:
        print("Not a valid option.")