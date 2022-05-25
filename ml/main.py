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

    for i in people.iterrows():
        current = ratings.loc[1:57, index]
        current = current.to_frame()
        for a in current.iterrows():
            print(a[1])


trainingFunc(ratings, movies, people)