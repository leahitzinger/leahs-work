from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler 
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
import os 
import logging
import os 
import pickle 

#removes outliers and prepares the data for training 
def clean_data(df):
    df.replace({False: 0, True: 1}, inplace=True)
    df=df.drop(columns='counter',axis=1)
    df=df[df['bathrooms']<3]
    df=df[df['bedrooms']<4]
    df.replace({'no': 0, 'yes': 1}, inplace=True)
    df=df.drop(['furnishingstatus','prefarea','hotwaterheating',
                'mainroad','guestroom'], axis=1)
    
    return df

def split_data(df,target):
    X=df.drop([target], axis=1)
    y =  df[target]
    X_train, X_test, y_train, y_test= train_test_split(X, y,shuffle=True,test_size=0.2)
    
    return X_train, X_test, y_train, y_test 

def scale_data(X_train, X_test):
    scaler = MinMaxScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled 
    
def instantiate_and_train_model(model,y_train,X_train_scaled):
    model = model
    model.fit(X_train_scaled, y_train)
    
    return model
    
def predict_model(model,X_test_scaled,y_test):  
    predictions = model.predict(X_test_scaled)
    score=r2_score( y_test,predictions)
    RMSE = mean_squared_error(y_test, predictions, squared = False)
    MAE = mean_absolute_error(y_test, predictions)
    
    return score,RMSE,MAE

def pickle_model(model_name,trained_model):
    clean_model_name='{}'.format(model_name).split("(")[0]
    with open(f"{str(model_name).split('(')[0]}.pkl", "wb") as file: # file is a variable for storing the newly created file, it can be anything.
        pickle.dump(trained_model, file)
    path=os.path.realpath(file.name)
    
    return clean_model_name, path 

def load_model(file_name):
    loaded_model = pickle.load(open(file_name, 'rb'))

    return loaded_model
    


# Takes all the steps needed to train a model and returns 
# a list of all infoyou want to insurt to the table   
def instantiate_model(model_name, df, target,):
    df=clean_data(df)
    X_train, X_test, y_train, y_test = split_data(df, target)
    X_train_scaled, X_test_scaled = scale_data(X_train, X_test)
    trained_model = instantiate_and_train_model(model_name, y_train,X_train_scaled,)
    score,  RMSE,MAE = predict_model(trained_model, X_test_scaled, y_test)
    clean_model_name, path=pickle_model (model_name,trained_model)
    features="{}".format(list(df.columns))
    val=(clean_model_name, 
    path ,features , score, 
    RMSE ,MAE )
    
    return val


def increment_model(model_path, df, target,):
    df=clean_data(df) 
    X_train, X_test, y_train, y_test = split_data(df, target)
    X_train_scaled, X_test_scaled = scale_data(X_train, X_test)
    loaded_model = load_model('SGDRegressor.pkl')
    loaded_model.partial_fit(X_train_scaled, y_train)
    score,  RMSE,MAE = predict_model(loaded_model, X_test_scaled, y_test)
    clean_model_name='{}'.format(model_path).split("(")[0]
    path=os.path.realpath(model_path)
    features="{}".format(list(df.columns))
    val=(clean_model_name, 
    path ,features , score, 
    RMSE ,MAE )
    return val

def create_logging():
    CURR_DIR = os.path.dirname(__file__)
    LOG_FOLDER =  CURR_DIR + '/logs'
    LOG_FILE = LOG_FOLDER + '/Housing_logs.txt'
    logging.basicConfig(filename= LOG_FILE,
                        filemode='a+',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.INFO)
    
    return logging