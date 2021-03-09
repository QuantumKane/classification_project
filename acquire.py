# imports needed
import pandas as pd
import numpy as np
import os
from env import host, user, password

def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
    

def get_telco_data():
    '''
    This function uses the SQL query from below and specifies the database to use
    '''
    # SQL query that joins all of the tables together from the 'telco_churn' database     
    sql_query = """
                SELECT * 
                FROM customers 
                JOIN payment_types USING (payment_type_id) 
                JOIN contract_types USING (contract_type_id) 
                JOIN internet_service_types USING (internet_service_type_id)
                """
    return pd.read_sql(sql_query,get_connection('telco_churn'))
