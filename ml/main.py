import pandas as pd

data = pd.read_csv('./ml/data.csv', sep=',', header=None)

ratings = data.loc[1:57, 4:24]
movies = data.loc[1:57, 2]
people = data.loc[0, 4:24]

movies = movies.to_frame()
people = people.to_frame()

print(people)
def trainingFunc(ratings, movies, people):
    index = 4
    print(ratings)
    result = pd.DataFrame()
    usertable = pd.DataFrame(data=1, index=range(21), columns=range(21))
    print(usertable)
    

    for i, row in ratings.iterrows():
        
        row = row.to_frame()

        for a, user in row.iterrows():
            result.at[i,a] = 5
            
            for b, user2 in row.iterrows():
                if b == a:
                    continue



trainingFunc(ratings, movies, people)