import pandas as pd
import numpy as np


'''
This is how I originally imported the data.
data = pd.read_csv('./ml/data.csv', sep=',', header=None)
ratings = pd.read_csv('./ml/ratings.csv', sep=',', header=None)
people = pd.read_csv('./ml/people.csv', sep=',', header=None)

movies = data.loc[1:57, 2]


ratings = ratings.astype(float)

ratings.to_numpy()

movies.to_frame()
'''

# Add numpy arrays here (ratings is just a rectangle of the numerical ratings, people is a row of initials and names, movies is a row of movie names):
'''
ratings = []
movies = []
people = []
'''

def guessRating(ratings, movies, people):
    
    # using pandas because I feel more comfortable with it
    result = pd.DataFrame()
    usertable = pd.DataFrame(data=3, index=range(people.shape[1]), columns=range(people.shape[1]))
    ratings = pd.DataFrame(ratings)
    print(people)

    # Uses a simplified version of collaborative filtering to determine which users like similar movies
    for i, row in ratings.iterrows():

        # sets "row" to a dataframe so I can iterate through it
        row = row.to_frame()
        for a, user in row.iterrows():
            index = 0

            # iterates through every user
            for b, user2 in row.iterrows():



                # makes sure it is not checking itself
                if b == a:
                    index += 1
                    continue

                # Makes sure that they actually rated the movie
                elif ratings.at[i,b] < 0:
                    index += 1
                    continue

                # If the rating is over 10, set it to 10
                elif ratings.at[i,b] > 10:
                    ratings.at[i,b] = 10
                

                # If the ratings are the same, add 2 to the similarity score
                if ratings.at[i,b] == ratings.at[i,a]:
                    usertable.at[a,index] = usertable.at[a,index] + 2
                # If they are within 2, add 1 to the similarity score
                elif ratings.at[i,b] < ratings.at[i,a] and ratings.at[i,b] > ratings.at[i,a] - 2 or ratings.at[i,b] > ratings.at[i,a] and ratings.at[i,b] < ratings.at[i,a] + 2:
                    usertable.at[a,index] = usertable.at[a,index] + 1
                # If they are far apart, subtract 1 from the similarity score
                else:
                    usertable.at[a,index] = usertable.at[a,index] - 1
                    
                index += 1



    # Iterates through every movie
    for i, row in ratings.iterrows():
        index = 0

        row = row.to_frame()


        # Creates the matches list, which will store the top 5 most similar people
        matches = [(-500, 0),(-500, 0), (-500, 0),(-500, 0),(-500, 0)]
        for c, row2 in usertable.iloc[0].items():
            
            # Makes sure that it is not checking itself
            if c == 0:
                continue

            # Makes sure that they actually rated the movie
            elif ratings.at[i,c] < 0:
                continue


            # If the person is more similar than someone in the top five, adjust accordingly
            if row2 > matches[0][0]:
                matches[4] = matches[3]
                matches[3] = matches[2]
                matches[2] = matches[1]
                matches[1] = matches[0]
                matches[0] = (row2, c)
            elif row2 > matches[1][0]:
                matches[4] = matches[3]
                matches[3] = matches[2]
                matches[2] = matches[1]
                matches[1] = (row2, c)
            elif row2 > matches[2][0]:
                matches[4] = matches[3]
                matches[3] = matches[2]
                matches[2] = (row2, c)
            elif row2 > matches[3][0]:
                matches[4] = matches[3]
                matches[3] = (row2, c)
            elif row2 > matches[4][0]:
                matches[4] = (row2, c)


        # Takes a weighted average of the top 5's ratings of the same movie
        index2 = 5
        weighted = [0,0,0,0,0]
        number = 0
        for d in matches:
            
            # If less than 5 people rated the movie, it will ignore the placeholder values
            if d[0] == -500:
                continue

            # Gets the person's rating of the movie
            point = ratings.at[i,d[1]]

            # Adds the rating to the weighted average
            weighted[matches.index(d)] = point * index2
            number += index2
            index2 -= 1

        # Divides the sum of the ratings by the number of times it was multiplied by to create the average
        if number != 0:
            result.at[i,0] = sum(weighted) / number
        # If no one else rated the movie, guess the rating is 6
        else:
            result.at[i,0] = 6


    

        # Does the same thing, but for the rest of the people
        for a, user in row.iterrows():


            matches = [(-500, 0),(-500, 0), (-500, 0),(-500, 0),(-500, 0)]

            for c, row2 in usertable.iloc[a].items():

                if c == a:
                    continue
                elif ratings.at[i,c] < 0:
                    continue



                if row2 > matches[0][0]:
                    matches[4] = matches[3]
                    matches[3] = matches[2]
                    matches[2] = matches[1]
                    matches[1] = matches[0]
                    matches[0] = (row2, c)
                elif row2 > matches[1][0]:
                    matches[4] = matches[3]
                    matches[3] = matches[2]
                    matches[2] = matches[1]
                    matches[1] = (row2, c)
                elif row2 > matches[2][0]:
                    matches[4] = matches[3]
                    matches[3] = matches[2]
                    matches[2] = (row2, c)
                elif row2 > matches[3][0]:
                    matches[4] = matches[3]
                    matches[3] = (row2, c)
                elif row2 > matches[4][0]:
                    matches[4] = (row2, c)

            index2 = 5
            weighted = [0,0,0,0,0]
            number = 0
            for d in matches:

                if d[0] == -500:
                    continue
                point = ratings.at[i,d[1]]

                weighted[matches.index(d)] = point * index2
                number += index2
                index2 -= 1

            if number != 0:
                result.at[i,a] = sum(weighted) / number
            else:
                result.at[i,a] = 6
    
            


    
    # Creates the dataframe that will be used to calculate the average difference between the predicted and actual ratings
    difference = pd.DataFrame(data=0, index=range(ratings.shape[0]), columns=range(ratings.shape[1]))

    # Iterates through every rating
    for i, row in ratings.iterrows():
        row = row.to_frame()
        for a, column in row.iterrows():

            # If the person has not rated the movie, it will not be included in the average
            if ratings.at[i,a] < 0:
                continue

            # Calculates the difference between the predicted and actual rating

            difference.at[i,a] = result.at[i,a] - ratings.at[i,a]

    # Calculates the average difference between the predicted and actual ratings
    mean = 0
    index = 0
    for i, row in difference.iterrows():
        row = row.to_frame()
        for a, column in row.iterrows():
            # Ignores data points that aren't ratings
            if difference.at[i,a] == 0:
                continue

            # Adds the difference to the mean
            mean += abs(difference.at[i,a])
            index += 1

    # Calculates the average difference
    mean = mean / index

    # Prints out and writes the results to a file
    print(result)
    print(difference)
    print(mean)

    result.to_csv('result.csv')
    difference.to_csv('difference.csv')
    f = open('mean.txt', 'x')
    f.write("mean:" + str(mean))
    f.close()
            
            


# Calls the function
guessRating(ratings, movies, people)