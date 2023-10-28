# Importing necessary modules
from .db import SqlHandler
from .logger import CustomFormatter
from .models import CLV


# Create an instance of SqlHandler
clv_handler_insert = SqlHandler('internet_service_provider', 'clv_prediction')

# Uncomment the next line if you want to truncate the table before inserting
#clv_handler.truncate_table()

# insert prediction to db
clv_instance = CLV()
clv_pred1 = clv_instance.CLV_formula()

clv_data1 = {
    "prediction_id": 1,
    "customer_id ": 1,
    "clv": clv_pred1,
}
clv_handler_insert.insert_one(clv_data1)
clv_handler_insert.close_cnxn()


# select data from db
clv_handler_select = SqlHandler('internet_service_provider', 'dim_customer')

# Uncomment the next line if you want to truncate the table before inserting
# clv_handler_select .truncate_table()

column_name = "gender"
value = "Female"
print(clv_handler_select.select_row(column_name, value))

clv_handler_select.close_cnxn()