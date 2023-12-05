# SocraCLV

### Group project within the scope of the course DS223 – Marketing Analytics

The project aims to develop a Python package for predicting a customer's Lifetime Value (CLV) for an Internet package provider that can be applied to similar-scope companies in general. As the name suggests, the package is not just about analytics but involves a philosophically flavoured approach to understanding and predicting Customer Lifetime Value to gain meaningful insights about the long-term relationships between the company and customers.


## SetUp

To get started, run 

```python -m clv.db.schema ``` to create the schema

```python basic_clv.py``` to load the data in the root of the repo

```python calculate_clv.py``` To calculate CLV and put into dataset
OR
```python -m clv.db.schema && python basic_clv.py && python calculate_clv.py```
and ```python -m clv.api.fast``` to run the api

To check the db follow the link https://inloop.github.io/sqlite-viewer/