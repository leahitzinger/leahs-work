import matplotlib.pyplot as plt
import seaborn as sns
from guided_project_function import catplot
from guided_project_function import catplotpoint

def new(b,c):
    a=c[c['is_canceled']==0]
    catplot(a,b)


def new2(a,b,c):
    print(c)
    catplotpoint(a,b)




