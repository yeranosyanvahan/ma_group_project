-- Create the Dim_Customer table
CREATE TABLE dim_customer (
    customer_id INT PRIMARY KEY,
    age INT,
    gender INT
);

-- Create the Dim_Payment_Method table
CREATE TABLE dim_payment_method (
    payment_method_id INT PRIMARY KEY,
    payment_method_name VARCHAR(255)
);

-- Create the Fact_Transacation table
CREATE TABLE fact_transacation (
    transaction_id INT PRIMARY KEY,
    customer_id INT,
    payment_method_id INT,
    transaction_date DATETIME,
    amount FLOAT,
    FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id),
    FOREIGN KEY (payment_method_id) REFERENCES dim_payment_method(payment_method_id)
);

-- Create the CLV_Prediction Table
CREATE TABLE clv_prediction (
    prediction_id SERIAL PRIMARY KEY,
    customer_id INT,
    clv FLOAT,
    FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id)
);