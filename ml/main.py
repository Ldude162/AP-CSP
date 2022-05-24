import tensorflow as tf
import pandas as pd

data = pd.read_csv('./ml/data.csv', sep=',', header=None)

training = data.loc[1:57, 4:14]
testing = data.loc[1:57, 15:24]
movies = data.loc[1:57, 2]
people = data.loc[0, 4:24]
print(people)
def training(trainData, movies, people):
    print(2)