from clv.models import CLV
from clv.db import SqlHandler
import pandas as pd
# Example usage:
if __name__ == "__main__":

    connect_to_dim_customer = SqlHandler('internet_service_provider', 'dim_customer')

    # Get transaction table data
    dim_customer = connect_to_dim_customer.get_table_data()
    connect_to_dim_customer.close_cnxn()

    dim_customer['clv'] = [CLV(t=5, customer_id=id).calculate_clv() for id in dim_customer['customer_id']]
    prediction = dim_customer[['clv','customer_id']].reset_index().rename(columns={'index': 'prediction_id'})
    labels = ["Lost Cause", "Free Rider", "Vulnerable", "Star"]
    prediction['predicted_customer_type'] = pd.qcut(prediction['clv'], 4, labels=labels)

    connect_to_prediction = SqlHandler('internet_service_provider', 'clv_prediction')

    # Get transaction table data
    dim_customer = connect_to_prediction.insert_many(prediction)
    connect_to_prediction.close_cnxn()