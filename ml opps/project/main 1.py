from connection1 import *
from functions1 import *
from query1 import *
import traceback
import pandas as pd
from sklearn.linear_model import LinearRegression


def main():
        try:
                logging=create_logging()
                df=pd.read_csv('Housing 1.csv')
                df=df.replace({ 'yes':True, 'no': False})
                db=Connection(host='localhost',port=3306,username='root',password='Qwerty613!', database='sakila')
                db.connect_to_database()
                logging.info('connected to database')
                db.create_database('housing_data')
                db.execute_query(housing)
                db.insert_df(df,'Housing')
                training_df=db.read_sql(get_80)
                val=instantiate_model(LinearRegression(), training_df,'price')
                logging.info('the model was trained')
                db.execute_query(models)
                db.add_model(val,insert_model)
                logging.info('the model was inserted to the database')
                db.conn.close()
        except Exception as e:
                '''This exception catches the errors and logs them.'''
                print ('There is an error'+str(e))
                logging.error('There is an error'
                +traceback.format_exc() + '{}'.format(str(e)))





       

if __name__ == '__main__':

    main()
   
