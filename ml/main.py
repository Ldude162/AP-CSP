import pandas as pd

data = pd.read_csv('data.csv', sep=',', header=None)



ratings = data.loc[1:57, 4:24]
movies = data.loc[1:57, 2]
people = data.loc[0, 4:24]

ratings = ratings.astype(float)


movies = movies.to_frame()
people = people.to_frame()

print(people)
def trainingFunc(ratings, movies, people):
    print(ratings)
    result = pd.DataFrame()
    usertable = pd.DataFrame(data=3, index=range(21), columns=range(21))
    print(usertable)
    
    multiplier = 1

    for i, row in ratings.iterrows():
        index = 0
        row = row.to_frame()
        for b, user2 in row.iterrows():

            newa = 0
            if b == 4:
                index += 1
                continue
            elif ratings.at[i,b] < 0:
                index += 1
                continue
            elif ratings.at[i,b] > 10:
                ratings.at[i,b] = 10
            
            if ratings.at[i,b] == ratings.at[i,4]:
                usertable.at[newa,index] = usertable.at[newa,index] + 2
            elif ratings.at[i,b] < ratings.at[i,4] and ratings.at[i,b] > ratings.at[i,4] - 2 or ratings.at[i,b] > ratings.at[i,4] and ratings.at[i,b] < ratings.at[i,4] + 2:
                usertable.at[newa,index] = usertable.at[newa,index] + 1
            else:
                usertable.at[newa,index] = usertable.at[newa,index] - 1
            print(usertable.at[newa,index])
            index += 1

        print(usertable)

        matches = [(-500, 0),(-500, 0), (-500, 0),(-500, 0),(-500, 0)]
        for c, row2 in usertable.iloc[0].items():
            print(c)
            if c == 0:
                continue
            elif ratings.at[1,c + 4] < 0:
                continue

            print(c)

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
        weighted = []
        number = 0
        for d in matches:
            print(d)
            if d[0] == -500:
                continue
            point = ratings.at[0,d[1] + 3]
            weighted[matches.index(d)] = point * index2
            number += index2
            index2 -= 1

        result.at[i,0] = sum(weighted) / number

        print(result.at[i,0])

    
        apple = "apple" / 0

        for a, user in row.iterrows():
            result.at[i,a] = 5
            index = 0
            
            for b, user2 in row.iterrows():

                newa = a - 4
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


    print(usertable)



trainingFunc(ratings, movies, people)