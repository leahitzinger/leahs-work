import pandas as pd
df=pd.read_csv('C:/Users/admin/Documents/guided project/Parallel Processing/lesson3/googleplaystore.csv')


def count_rating(ratings):
    people_in_ratings={}
    for rating_name in ratings:
        people_in_ratings[rating_name]=df['Category'].str.count(rating_name).sum()
    print(people_in_ratings ) 
ratings=df['Category'].unique()
count_rating(ratings)

