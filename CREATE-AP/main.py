'''
Grocery list program for AP CREATE task
'''

# Import OS module
import os

# Set variable for while loop
cont = True

'''
Opens a list for editing and viewing
'''
def openList(list):

    # Opens the list and prints it
    f = open(list + '.txt', 'r')
    print("Here is the elements in the list " + list + ":")
    print(f.read())
    f.close()

    # Checks if the user wants to add something to the list, and if so asks them what and adds it
    add = 'y'

    while add == 'y':

        add = input("Do you want to add something to the list? (y/n) ")

        if add == "y":

            item = input("What do you want to add? ")

            # Code for adding the item
            f = open(list + '.txt', 'a')
            f.write(item + "\n")
            f.close()
            print("Item added!")
    
    # Checks if the user wants to delete something from the list, and if so asks them what and deletes it.
    delete = 'y'

    while delete == 'y':

        delete = input("Do you want to delete something from the list? (y/n) ")

        if delete == "y":

            item = input("Which item do you want to delete? Enter the item exactly as it is in the list. ")
            f = open(list + '.txt', 'r')

            # Gets a list with every line of the grocery list
            lines = f.readlines()
            f.close()
            f = open(list + '.txt', 'w')

            # For every line...
            for line in lines:
                # ... if the line is not the item being deleted, put it back in the grocery list
                if line != item + '\n':
                    f.write(line)
            f.close()

            # Prints out the finished grocery list.
            print("Your list now looks like this:")
            f = open(list + '.txt', 'r')
            print(f.read())
            f.close()


# Main loop for the program
while cont:

    # Asks the user what they want to do
    option = input("What would you like to do? (n for new list, v for view, add to, or remove things from an existing list, d to delete a list, or type e to exit the program. ")

    # If they want to make a new list...
    if option == "n":

        # Asks them what they want the new list to be called
        name = input("What do you want to name the new list? ")

        # If it already exists, tell them so and move on
        if os.path.exists(name + '.txt'):
            print("That list already exists.")

        # If it can be created...
        else:
            f = open(name + '.txt', 'x')
            f.close()

            # Ask them what they want the first item to be.
            add = input("List " + name + " created. What is the first thing you want to add to the list? ")

            f = open(name + '.txt', 'a')
            f.write(add + '\n')
            f.close()
    
    # If they want to view a list
    elif option == "v":

        # Print out all of the existing lists
        print("Current lists:")

        for files in os.listdir():

            if files.endswith('.txt'):
                files = files.split('.txt')
                print(files[0])
        
        # Asks them which list they want to view
        list = input("Which list would you like to view? ")

        #Checks if it exists, and if so opens it.
        if os.path.exists(list + '.txt'): 
            openList(list)    

        # If not, let the user know.    
        else:
            print("Hmm... I couldn't find this list. Are you sure you spelled it correctly?")
    
    # If they want to delete a list
    elif option == 'd':

        # Print out all of the current lists
        print("Current lists:")

        for files in os.listdir():

            if files.endswith('.txt'):
                files = files.split('.txt')
                print(files[0])

        # Asks them which one they want to delete
        list = input("Which list would you like to delete? ")

        # Deletes it, if it exists
        if os.path.exists(list + '.txt'):
            os.remove(list + '.txt')
            print("List " + list + " deleted.")

        # If not, let the user know.
        else:
            print("Hmm... I couldn't find this list. Are you sure you spelled it correctly?")

    # If the user wants to quit the program, do that.
    elif option == 'e':
        
        cont = False

    # If the user has not entered a valid option, let them know.
    else:
        print("Not a valid option.")