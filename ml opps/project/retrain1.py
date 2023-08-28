from sklearn.linear_model import SGDRegressor
from connection1 import *
from functions1 import *
from query1 import *


def main():   
    logging=create_logging()
    db=Connection(host='localhost',port=3306,username='root',
                  password='Qwerty613!', database='sakila')
    db.connect_to_database()
    logging.info('connected to database')
    db.create_database('housing_data')
    increment_df=db.read_sql(get_20)
    training_df=db.read_sql(get_80)
    val=instantiate_model(SGDRegressor(warm_start=True), training_df,'price')
    logging.info('the model was trained')
    db.add_model(val,insert_model)
    logging.info('the model was inserted to the database')
    val=increment_model('SGDRegressor.pkl',
                        increment_df, 'price')
    logging.info('the model was incremented')
    db.add_model(val,insert_model)    
    logging.info('the  incremented model was inserted to the database')
if __name__ == '__main__':
    main()





















































































































