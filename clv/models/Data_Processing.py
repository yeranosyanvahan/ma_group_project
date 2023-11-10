from ..db import SqlHandler
from ..logger import CustomFormatter
from ..models import CLV
import pandas as pd
import numpy as np
from datetime import datetime
from lifelines import KaplanMeierFitter

# Create an instance of SqlHandler
clv_handler = SqlHandler('internet_service_provider', 'fact_transaction')

# Get transaction table data
data = clv_handler.get_table_data()
clv_handler.close_cnxn()



# Convert 'transaction_date' to datetime
data['transaction_date'] = pd.to_datetime(data['transaction_date'])


def MM():
    """
    Calculate the average monthly margin based on the last year's transaction data.

    Returns:
    -------
    float:
        The calculated average monthly margin.
    """

    # Filter the data for the previous year
    prev_year = data['transaction_date'].dt.year.max()-1
    filtered_data = data[data['transaction_date'].dt.year == prev_year]

    # Group the data by month and calculate the sum of revenue
    monthly_sum = filtered_data.groupby(filtered_data['transaction_date'].dt.month)['amount'].sum()

    # Calculate the average monthly margin for the previous year
    average_monthly_margin = np.sum(monthly_sum)/12

    return average_monthly_margin

def p(t):
    """
    Calculate the survival probabilities for customers at time t using Kaplan-Meier estimator.

    Parameters:
    -----------
    t : int
        Time for which survival probabilities are calculated.

    Returns:
    --------
    list:
        A list of survival probabilities at different time points up to t.
    """

    data['transaction_date'] = pd.to_datetime(data['transaction_date'])

    # Group the data by customer and find the latest transaction date
    data["customer_latest_transaction"] = data.groupby('customer_id')['transaction_date'].transform('max')
    data['customer_earliest_transaction'] = data.groupby('customer_id')['transaction_date'].transform('min')
    data['survival_time_months'] = (data['customer_latest_transaction'] - data['customer_earliest_transaction']).dt.days // 30
    # Get the current date
    current_date = datetime.now()

    # Calculate the event_observed column
    data['event_observed'] = (
            (current_date.year != data['customer_latest_transaction'].dt.year) |
            (current_date.month != data['customer_latest_transaction'].dt.month)).astype(int)

    data.drop_duplicates(subset='customer_id', keep='first', inplace = True)

    kmf = KaplanMeierFitter()
    kmf.fit(durations=data["survival_time_months"], event_observed=data["event_observed"])

    kmf_table = kmf.event_table

    # Get survival probability at time t

    time_points = kmf_table.index.tolist()
    for i, time_point in enumerate(time_points):
        if t >= time_points[-1]:
            time_range_index = len(time_points) - 1
        if t >= time_point and (i + 1 < len(time_points) and t < time_points[i + 1]):
            time_range_index = i
            break

    probability_list = [1]

    for time in range(time_range_index):
        event_at_t = kmf_table.iloc[time, :]
        survival_prob_at_t = ((event_at_t.at_risk - event_at_t.observed) / event_at_t.at_risk) * probability_list[-1]
        probability_list.append(survival_prob_at_t)

    return probability_list

