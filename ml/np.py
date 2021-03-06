import pandas as pd


data = pd.read_csv('./ml/data.csv', sep=',', header=None)



ratings = data.loc[1:57, 4:24]
movies = data.loc[1:57, 2]
people = data.loc[0, 4:24]

ratings = ratings.astype(float)

ratings = ratings.to_numpy()

movies = movies.to_frame()
people = people.to_frame()

print(people)
def guessRating(ratings, movies, people):
    

    ratings = pd.DataFrame(ratings)


    result = pd.DataFrame(data=0, index=range(57), columns=range(20))
    usertable = pd.DataFrame(data=3, index=range(21), columns=range(21))
   
    
    multiplier = 1

    for i, row in ratings.iterrows():

        row = row.to_frame()
        for a, user in row.iterrows():
            index = 0

            for b, user2 in row.iterrows():
                newa = a
                if b == a:
                    index += 1
                    continue
                elif ratings.at[i,b] < 0:
                    index += 1
                    continue
                elif ratings.at[i,b] > 10:
                    ratings.at[i,b] = 10
                
                if ratings.at[i,b] == ratings.at[i,a]:
                    usertable.at[newa,index] = usertable.at[newa,index] + 2
                elif ratings.at[i,b] < ratings.at[i,a] and ratings.at[i,b] > ratings.at[i,a] - 2 or ratings.at[i,b] > ratings.at[i,a] and ratings.at[i,b] < ratings.at[i,a] + 2:
                    usertable.at[newa,index] = usertable.at[newa,index] + 1
                else:
                    usertable.at[newa,index] = usertable.at[newa,index] - 1
                    
                index += 1




    for i, row in ratings.iterrows():
        index = 0
        row = row.to_frame()



        matches = [(-500, 0),(-500, 0), (-500, 0),(-500, 0),(-500, 0)]
        for c, row2 in usertable.iloc[0].items():

            if c == 0:
                continue
            elif ratings.at[i,c] < 0:
                continue

            print(row2)

            if row2 > matches[0][0]:
                matches[4] = matches[3]
                matches[3] = matches[2]
                matches[2] = matches[1]
                matches[1] = matches[0]
                matches[0] = (row2, c)
                print(matches[0])
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

        result.at[i,0] = sum(weighted) / number



    


        for a, user in row.iterrows():

            newa = a - 4
            matches = [(-500, 0),(-500, 0), (-500, 0),(-500, 0),(-500, 0)]

            for c, row2 in usertable.iloc[newa].items():

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
            result.at[i,a] = sum(weighted) / number
    
            


    print(result)

    difference = pd.DataFrame(data=0, index=range(57), columns=range(21))

    for i, row in ratings.iterrows():
        row = row.to_frame()
        for a, column in row.iterrows():
            if ratings.at[i,a] < 0:
                continue
            difference.at[i,a] = result.at[i,a] - ratings.at[i,a]
    mean = 0
    index = 0
    for i, row in difference.iterrows():
        row = row.to_frame()
        for a, column in row.iterrows():
            if difference.at[i,a] == 0:
                continue

            mean += abs(difference.at[i,a])
            index += 1

    mean = mean / index

    print(difference)
    print(mean)
            
            



guessRating(ratings, movies, people)