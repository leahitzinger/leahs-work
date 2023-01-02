import matplotlib.pyplot as plt
import pandas as pd
from analysis_fun import clean
from analysis_fun import fun
from plotting_fun import catplotpoint
from plotting_fun import catplotcis_c

hotel=pd.read_csv('C:/Users/admin/Documents/guided project/guided-project/hotel_bookings.csv')

clean(hotel,'adults')
clean(hotel,'babies')
clean(hotel,'children')


adults_1=fun(hotel,'adults')
children_1=fun(hotel,'babies')
babies_1=fun(hotel,'children')

people=pd.concat([adults_1,children_1,babies_1], axis=0)

catplotcis_c('count of arrivals per year',people)

catplotpoint(people,'people')


