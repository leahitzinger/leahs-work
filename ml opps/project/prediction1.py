from connection import *
from functions import *
from query import *
import pickle
import numpy as np
from sklearn.linear_model import LinearRegression



def get_predictions1():
    area=int(input('Please insert area number'))
    bedrooms=int(input('Please insert number of bedrooms'))
    bathrooms=int(input('Please insert number of bathdrooms'))
    stories=int(input('Please insert number of stories'))
    basement=int(input('Please insert 0 or 1'))
    airconditioning=int(input('Please insert 0 or 1'))
    parking=int(input('Please insert number of parking'))
    data = np.array([area,bedrooms,bathrooms,stories,basement,airconditioning,parking])
    data=data.reshape(1,7) 
    loaded_model = pickle.load(open('logistic_regression.pkl', 'rb'))
    prediction=loaded_model.predict(data)
    print(prediction)
 
get_predictions1()   
