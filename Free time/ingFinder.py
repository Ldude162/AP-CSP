#Import module (duh)
import requests as req

#api links
api = "https://api.wynncraft.com/v2/ingredient/list"
apiSearch = "https://api.wynncraft.com/v2/ingredient/search/name/"

#Trys to make a file, if it already exists it doesn't make a new one
try:
    #tries making a file, throws an error if it exists
    file = open('test.txt', 'x')
    #Writes data to the file
    file.write(str(req.get(api).json()))
    #Closes file
    file.close()
except:
    #opens file
    file = open('test.txt')

#Reads file
ings = file.read()
file.close()

#Asks the user what ingredient they want to look for
search = input("Type in the first few letters of the ingredient you want to search")

#Checks the length of the search to make sure it's not too small
if len(search) < 3:
    #Error message
    print("Couldn't find the ingredient! Try typing more letters!")
    #Checks that it is an actual ingredient
elif ings.lower().__contains__(search.lower()):
    #Gets the stats of the ingredients searched
    searchResults = req.get(apiSearch + search).json()
    
    #prints the results for the search
    print("Results for", search + ':')
    for i in searchResults['data']:
        #Prints name, tier, level, and skills of the ingredient
        print('Name:', i['name'], '| Tier:', i['tier'], '| Level:', i['level'], '| Skills:', i['skills'])
        #Prints ID's and their min/max values
        print("ID's:")
        for a in i['identifications']:
            print(a+ ':', 'Minimum:', i['identifications'][a]['minimum'], '| Maximum:', i['identifications'][a]['maximum']) 
else:
    #If the ingredient is not found in the list, this error gets triggered
    print("Can't find this ingredient! Try checking the spelling and leaving out apostrophes!")
