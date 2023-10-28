# Importing necessary modules
from clv.db import SqlHandler
from clv.logger import CustomFormatter
import pandas as pd

# For dim_customer table
customer_handler = SqlHandler('internet_service_provider', 'dim_customer')
customer_data = pd.read_csv('dim_customer.csv')
# Uncomment the next line if you want to truncate the table before inserting
# customer_handler.truncate_table()
customer_handler.insert_many(customer_data)
customer_handler.close_cnxn()

# For dim_payment_method table
payment_method_handler = SqlHandler('internet_service_provider', 'dim_payment_method')
payment_method_data = pd.read_csv('dim_payment_method.csv')
# Uncomment the next line if you want to truncate the table before inserting
# payment_method_handler.truncate_table()
payment_method_handler.insert_many(payment_method_data)
payment_method_handler.close_cnxn()

# For fact_transaction table
transaction_handler = SqlHandler('internet_service_provider', 'fact_transaction')
transaction_data = pd.read_csv('fact_transaction.csv')
# Uncomment the next line if you want to truncate the table before inserting
# transaction_handler.truncate_table()
transaction_handler.insert_many(transaction_data)
transaction_handler.close_cnxn()

