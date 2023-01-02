import matplotlib.pyplot as plt
import seaborn as sns


def catplot(a,b):
    sns.catplot(data=a, col='people',x='arrival_date_year',kind='count',hue='hotel')
    plt.suptitle(b, y=1.1)

def catplotcis_c(b,c):
    a=c[c['is_canceled']==0]
    catplot(a,b)
    plt.savefig(b+'.png')
    

def catplotpoint(a,b):
    sns.catplot(data=a ,x=b ,y='is_canceled', kind='point',hue='hotel')
    plt.suptitle('percent of canceled {} arrivals per hotel'.format(b), y=1.1)
    plt.savefig(b+'.png')
