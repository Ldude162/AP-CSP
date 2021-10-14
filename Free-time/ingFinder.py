#Import module (duh)
import requests as req

#api links
api = "https://api.wynncraft.com/v2/ingredient/list"
apiSearch = "https://api.wynncraft.com/v2/ingredient/search/name/"

#Asks the user what ingredient they want to look for
search = input("Type in the first few letters of the ingredient you want to search")

#Checks the length of the search to make sure it's not too small
if len(search) < 3:
    #Error message
    print("Couldn't find the ingredient! Try typing more letters!")
    #Checks that it is an actual ingredient
else:
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
