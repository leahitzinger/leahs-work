#creates the housing table
housing='''CREATE TABLE IF NOT EXISTS Housing
(price float, area bigint UNSIGNED , 
bedrooms  bigint UNSIGNED, 
bathrooms bigint UNSIGNED,
stories  mediumint UNSIGNED ,
mainroad bool, guestroom bool,basement bool,
hotwaterheating bool,airconditioning BOOL,
parking mediumint UNSIGNED,
prefarea BOOL, furnishingstatus VARCHAR(50))'''

#gets 80% of the database 
get_80='''SELECT*
     FROM    (
    SELECT Housing.*, @counter := @counter +1 AS counter
    FROM (select @counter:=0) AS initvar, Housing
) AS X
where counter <= (80/100 * @counter);'''

#gets 20% of the database 
get_20='''SELECT*
     FROM    (
    SELECT Housing.*, @counter := @counter +1 AS counter
    FROM (select @counter:=0) AS initvar, Housing
) AS X
where counter > (80/100 * @counter);'''


#creates the model table with 
models='''CREATE TABLE IF NOT EXISTS save_models
( model_id  int primary key auto_increment ,
model_name varchar(500) , 
path VARCHAR(500), 
features  varchar(5000),
r2_score decimal (30,20), 
RMSE   decimal (30,20),
MAE  decimal (30,20) ) 
'''

#inserts the model into the table
insert_model='''INSERT INTO save_models 
    (model_name , 
    path ,features ,r2_score, 
    RMSE ,MAE)   VALUES (%s, %s,%s, %s,%s, %s)'''

