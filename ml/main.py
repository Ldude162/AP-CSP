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

    result = pd.DataFrame()
    print(result)

    for i in ratings.iterrows():
        print(i[2])
        #for a in i:
            


trainingFunc(ratings, movies, people)