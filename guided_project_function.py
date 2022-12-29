import matplotlib.pyplot as plt
import seaborn as sns
def catplot(a,b):
    sns.catplot(data=a, col='people',x='arrival_date_year',kind='count',hue='hotel')
    plt.suptitle(b, y=1.1)



def catplotpoint(a,b):
    sns.catplot(data=a ,x=b ,y='is_canceled', kind='point',hue='hotel')
    plt.suptitle('percent of canceled {} arrivals per hotel'.format(b), y=1.1)