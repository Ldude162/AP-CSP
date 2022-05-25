import pandas as pd

data = pd.read_csv('./ml/data.csv', sep=',', header=None)



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
        
        row = row.to_frame()

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