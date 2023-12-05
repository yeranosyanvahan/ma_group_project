
# SqlHandler Class Documentation

## Overview
The `SqlHandler` class is designed to handle common SQL operations on a database. It provides methods for various database operations such as inserting data, retrieving table columns, truncating tables, and more.

### Class Attributes:
- `dbname` (str): The name of the database.
- `table_name` (str): The name of the table to perform operations on.

## Methods

### `__init__(self, dbname: str, table_name: str) -> None`
Initializes the SqlHandler object with a database name and table name.

#### Parameters:
- `dbname` (str): The name of the database to connect to.
- `table_name` (str): The name of the table to perform operations on.

---

### `close_cnxn(self) -> None`
Closes the connection to the database.

---

### `insert_one(self, values: dict) -> str`
Inserts a single row into the table.

#### Parameters:
- `values` (dict): A dictionary containing the column names and their respective values.

#### Returns:
- A message indicating the success of the insertion.

---

### `get_table_columns(self) -> list`
Retrieves a list of column names from the table in the database.

#### Returns:
- A list of column names from the table.

---

### `truncate_table(self) -> None`
Removes all data from the table by dropping it and creating a new one.

---

### `drop_table(self)`
Drops the table from the database.

---

### `insert_many(self, df: pd.DataFrame) -> str`
Inserts multiple rows into the table from a Pandas DataFrame.

#### Parameters:
- `df` (pd.DataFrame): The DataFrame containing the data to insert.

#### Returns:
- A message indicating the success or failure of the operation.

---

### `from_sql_to_pandas(self, chunksize: int, id_value: str) -> pd.DataFrame`
Retrieves data from the table in chunks and returns it as a Pandas DataFrame.

#### Parameters:
- `chunksize` (int): The size of each data chunk to retrieve.
- `id_value` (str): The ID value to order the data by.

#### Returns:
- A DataFrame containing the retrieved data.

---

### `update_table(self, condition)`
Updates the table based on the specified condition.

#### Parameters:
- `condition`: The condition for updating the table.

---

### `select_row(self, column_name: str, value) -> tuple`
Selects a row from the table based on a specific column name and value.

#### Parameters:
- `column_name` (str): The name of the column to filter on.
- `value`: The value to filter rows by in the specified column.

#### Returns:
- A tuple containing the selected row.

---

### `get_table_data(self, columns: list = None, condition: str = None) -> pd.DataFrame`
Retrieves data from the table based on specified columns and an optional condition.

#### Parameters:
- `columns` (list): A list of column names to retrieve.
- `condition` (str): An optional SQL condition to filter the data.

#### Returns:
- A DataFrame containing the retrieved data.
