# FastAPI Routes Documentation

## Overview

This documentation covers the FastAPI routes used for handling various entities in the internet service provider's database. These entities include transactions, payment methods, customers, and CLV predictions.

### Transactions

#### Get a Transaction
- **Route**: `/transaction/{transaction_id}`
- **Method**: GET
- **Description**: Retrieve a transaction by its ID.

#### Create a Transaction
- **Route**: `/transaction/`
- **Method**: POST
- **Description**: Create a new transaction.

#### Update a Transaction
- **Route**: `/transaction/{transaction_id}`
- **Method**: PUT
- **Description**: Update an existing transaction.

#### Delete a Transaction
- **Route**: `/transaction/{transaction_id}`
- **Method**: DELETE
- **Description**: Delete a transaction.

### Payment Methods

#### Get a Payment Method
- **Route**: `/payment_method/{payment_method_id}`
- **Method**: GET
- **Description**: Retrieve a payment method by its ID.

#### Create a Payment Method
- **Route**: `/payment_method/`
- **Method**: POST
- **Description**: Create a new payment method.

#### Update a Payment Method
- **Route**: `/payment_method/{payment_method_id}`
- **Method**: PUT
- **Description**: Update an existing payment method.

#### Delete a Payment Method
- **Route**: `/payment_method/{payment_method_id}`
- **Method**: DELETE
- **Description**: Delete a payment method.

### Customers

#### Get a Customer
- **Route**: `/customer/{customer_id}`
- **Method**: GET
- **Description**: Retrieve a customer by their ID.

#### Create a Customer
- **Route**: `/customer/`
- **Method**: POST
- **Description**: Create a new customer.

#### Update a Customer
- **Route**: `/customer/{customer_id}`
- **Method**: PUT
- **Description**: Update an existing customer.

#### Delete a Customer
- **Route**: `/customer/{customer_id}`
- **Method**: DELETE
- **Description**: Delete a customer.

### CLV Predictions

#### Get a CLV Prediction
- **Route**: `/clv/{prediction_id}`
- **Method**: GET
- **Description**: Retrieve a CLV prediction by its ID.

#### Create a CLV Prediction
- **Route**: `/clv/`
- **Method**: POST
- **Description**: Create a new CLV prediction.

#### Update a CLV Prediction
- **Route**: `/clv/{prediction_id}`
- **Method**: PUT
- **Description**: Update an existing CLV prediction.

#### Delete a CLV Prediction
- **Route**: `/clv/{prediction_id}`
- **Method**: DELETE
- **Description**: Delete a CLV prediction.

### `read(db: Session, model, condition)`
Reads an object from the database using a condition.

#### Parameters:
- `db` (Session): The database session.
- `model`: The model class to query.
- `condition`: The condition to filter by.

#### Returns:
- The first object that matches the condition or None if not found.

## Additional Functions
### `create(db: Session, model, obj_data: dict)`
Creates a new object in the database.

#### Parameters:
- `db` (Session): The database session.
- `model`: The model class to create.
- `obj_data` (dict): The data to create the new object with.

#### Returns:
- The newly created object.

---

### `update(db: Session, model, condition, obj_data: dict)`
Updates an object in the database that matches a condition.

#### Parameters:
- `db` (Session): The database session.
- `model`: The model class to update.
- `condition`: The condition to filter by.
- `obj_data` (dict): The data to update the object with.

#### Returns:
- The updated object or None if not found.

---

### `delete(db: Session, model, condition)`
Deletes an object from the database that matches a condition.

#### Parameters:
- `db` (Session): The database session.
- `model`: The model class to delete from.
- `condition`: The condition to filter by.

#### Returns:
- True if the object was deleted, False otherwise.


## Example HTTP Requests

### GET example of clv prediction table
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/clv/2' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json'
```

### POST example of clv prediction table
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/clv/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
"prediction_id": 9999,
"customer_id": 1,
"clv" :200,
"predicted_customer_type": "Lost Cause",
"is_campaign1_success": true,
"is_campaign2_success": true

}  '
```

### PUT example of clv prediction table
```bash
curl -X 'PUT' \
  'http://127.0.0.1:8000/clv/10' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
"clv" :200,
"predicted_customer_type": "Vulnerable Customer",
"is_campaign1_success": true,
"is_campaign2_success": true
}'
```

### DELETE example data from clv prediction table
```bash
curl -X 'DELETE' \
  'http://127.0.0.1:8000/clv/2' \
  -H 'accept: application/json'

```