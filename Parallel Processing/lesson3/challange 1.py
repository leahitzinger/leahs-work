import pandas as pd
df=pd.read_csv('C:/Users/admin/Documents/guided project/Parallel Processing/lesson3/TopRichestInWorld.csv')
print(df[df['Industry']=='Technology'].count())
industries={}
