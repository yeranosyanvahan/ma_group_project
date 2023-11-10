# CLV Prediction for Internet Service Provider Company

### Group project within the scope of the course DS223 – Marketing Analytics

The project aims to develop a Python package for predicting a customer's Lifetime Value (CLV) for an Internet package provider. The CLV predictor will help understand the expected revenue from each customer over time, assisting in making informed strategic decisions. 


## Milestone 1

Virtual environment initiation: ```requirements.txt ```

Project-related documents: MoSCoW, Roadmap, ProblemDefinition, Database ERD


## Milestone 2

```docs```: project-related documents

```data```: project data

```clv```:

   ```api```: placeholder for API development components of the project

   ```db```: placeholder for Database development components of the project 

   ```models```: placeholder for the modeling-related classes, functions

   ```logger```: placeholder for logger module-related components


## Milestone 3

Defining business scenarios where the package for predicting Customer Lifetime Value (CLV) can be applied ```docs/DS223_Group5_ApplicationScenarios.pdf```


## SetUp

To get started, run 

```python -m clv.db.schema ``` to create the schema

```python basic_clv.py``` to load the data in the root of the repo

and ```python -m clv.api.fast``` to run the api

To check the db follow the link https://inloop.github.io/sqlite-viewer/

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
"is_campaign1_succes": true,
"is_campaign2_succes": true

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
"is_campaign1_succes": true,
"is_campaign2_succes": true
}'
```

### DELETE example data from clv prediction table
```bash
curl -X 'DELETE' \
  'http://127.0.0.1:8000/clv/2' \
  -H 'accept: application/json'

```
*Note: The current README.md file aims to coordinate the folders of project components in a simple manner. Along with further milestones and when the project is complete, it will be adapted to the required standards, integrating the processes of installation, usage, features, etc.* 