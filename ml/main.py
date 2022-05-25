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
    print(type(ratings))
    result = pd.DataFrame()
    print(result)

    for i, row in ratings.iterrows():
        print(row[0])
            


trainingFunc(ratings, movies, people)