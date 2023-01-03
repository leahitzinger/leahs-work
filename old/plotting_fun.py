import matplotlib.pyplot as plt
import seaborn as sns


def catplotcount(df,title,split_on,color):
    sns.catplot(data=df, col=split_on,x='arrival_date_year',kind='count',hue=color)
    plt.suptitle(title, y=1.1)
    plt.savefig(title+'.png')

def catplotcis_cancel(olddf,title,split_on,color,): 
    df=olddf[olddf['is_canceled']==0]
    catplotcount(df,title,split_on,color)
   
    

def catplotpoint(df,col1,col2,color,title):
    sns.catplot(data=df ,x=col1 ,y=col2, kind='point',hue=color)
    plt.suptitle('percent of canceled {} arrivals per hotel'.format(col1), y=1.1)
    plt.savefig(title+'.png')
