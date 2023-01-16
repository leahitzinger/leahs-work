# imported all fun. 
import matplotlib.pyplot as plt
import pandas as pd
from analysis_fun import cleans_nans,duplicating_rows,counts_values
from plotting_fun import catplotcis_cancel,catplotcount,catplotpoint


# reading in the dataframe
hotel=pd.read_csv('C:/Users/admin/Documents/guided project/old/hotel_bookings.csv')


# c=counts_values(hotel,'company',False)

# cleaning  the nans for adults, babies and children column 
cleans_nans(hotel,['adults','babies','children'],0)


# creating new data frame for each of those columns
#duplicating the dataframe acording to value in column
#renaming that column and its values
adults_1=duplicating_rows(hotel,'adults','people') 
children_1=duplicating_rows(hotel,'babies','people')
babies_1=duplicating_rows(hotel,'children','people')

#concating those three dataframes into one
people_df=pd.concat([adults_1,children_1,babies_1],axis=0)

#plotting a catplot of arrivals per year for canceled bookings
catplotcis_cancel(people_df,'count of arrivals per year','people','hotel')


#percent of canceled arrivals per hotel
catplotpoint(people_df,'people','is_canceled','hotel','percent of canceled arrivals per hotel')

#plotting a catplot of arrivals per year
catplotcount(people_df,'count of arrivals per year (including canceled)','people','hotel')



