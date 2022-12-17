# SQL BOLT

## 1.  SELECT queries

select specific columns from table, multiple columns can be selected by using comma

``` SQL
SELECT column, column ... FROM tableName;
```

 to select all coluns from table

 ```SQL
 SELECT * FROM tableName;
 ```

![1](/401/screenshots/sql1.png)

## 2. Constraints (meet these conditions)

 filter certain results using `WHERE` and `AND` `OR` to meet constraints

 |OPERATOR| CONDITION| EX.|
 | =, !=, < <=, >, >= | Standard numerical operators|columnName != 4|
 |BETWEEN … AND …|Number is within range of two values (inclusive)| columnName BETWEEN 1.5 AND 10.5|
 |IN (…)|Number exists in a list|columnName IN (2, 4, 6)|
 |NOT IN (…)|Number does not exist in a list|columnName NOT IN (1, 3, 5)|

### EXAMPLE SQL TABLE

 Table: Pets

 |Animal|legs|fur|
 |cat| 4| yes|
 |spider|8|no|
 |fish|0|no|
 |parakeet| 2|no|
 |dog|4|yes|
 |pigeon|2|no|
 |snake|0|no|

 return animals with 4 legs

 `SELECT Animal FROM Pets WHERE legs = 4 ;`

 return animals with no fur and more than 0 legs

 `SELECT Animal FROM Pets WHERE legs >0 AND fur= no;`

![2](/401/screenshots/sql2.png)

## 3. Queries with more Constraints

|OPERATOR| CONDITION | EXAMPLE |
| LIKE| Case insensitive exact string comparison|col_name LIKE "ABC"|
|NOT LIKE|Case insensitive exact string inequality comparison|col_name NOT LIKE "ABCD"|
|%|Used anywhere in a string to match a sequence of zero or more characters (only with LIKE or NOT LIKE)|col_name LIKE "%AT%"(matches "AT", "ATTIC", "CAT" or even "BATS")|
|_|Used anywhere in a string to match a single character (only with LIKE or NOT LIKE)|col_name LIKE "AN_"(matches "AND", but not "AN")|

### example using Pets table above

return animals that contain "ke" (snake, parakeet)

`SELECT Animal FROM Pets WHERE Animals LIKE "%ke%"`

![3](/401/screenshots/sql3.png)

## 4. Filtering and Sorting Results

- `DISTINCT` removes duplicate rows.
- `ORDER BY` sorts results in ascending or descending order, sorted alpha-numerically
- `LIMIT` reduce number of rows returned
- `OFFSET`  specifies where to begin counting the number rows from

### example using Pets table

return animals in ascending order

`SELECT Animal FROM Pets ORDER BY Animal ASC;`

![4](/401/screenshots/sql4.png)

## 5. REVIEW

![5](/401/screenshots/sql5.png)

## 6. Multi-table queries with JOINs

JOIN clause in a query, we can combine row data across two separate tables using this unique key

- `INNER JOIN otherTable` matches row from first table to second table mentioned
- `ON currentTable.colName = otherTable.colName` matches columns by name and combienes them in the query

![6](/401/screenshots/sql6.png)

## 13. Inserting Rows

- Schema describes the table structure and datatypes of each column.
- `INSERT` declares which table to write into, the columns of data that we are filling, and one or more rows of data to insert

```SQL
INSERT INTO mytable
VALUES (value_or_expr, another_value_or_expr, …),
       (value_or_expr_2, another_value_or_expr_2, …),
       …;
```

```SQL
INSERT INTO boxoffice
(movie_id, rating, sales_in_millions)
VALUES (1, 9.9, 283742034 / 1000000);
```

```SQL
INSERT INTO movies VALUES (4, "Toy Story 4", "El Directore", 2015, 90);

```

![13](/401/screenshots/sql13.png)

## 14. Updating Rows

`UPDATE` specify exactly which table, columns, and rows to update. In addition, the data you are updating has to match the data type of the columns in the table schema

```SQL
UPDATE mytable
SET column = value_or_expr, 
    other_column = another_value_or_expr, 
    …
WHERE condition;
```
![14](/401/screenshots/sql14.png)

## 15. Deleting Rows

`DELETE` delete data from table, use `WHERE`

```SQL
DELETE FROM mytable
WHERE condition;
```

![15](/401/screenshots/sql15.png)

## 16. Creating Tables

`CREATE TABLE` optional `IF NOT EXISTS`

- table schema, which defines a series of columns. Each column has a name, the type of data allowed in that column, an optional table constraint on values being inserted, and an optional default value

```SQL
CREATE TABLE IF NOT EXISTS mytable (
    column DataType TableConstraint DEFAULT default_value,
    another_column DataType TableConstraint DEFAULT default_value,
    …
);
```

```SQL
CREATE TABLE Database (
    Name TEXT,
    Version FLOAT,
    Download_count INTEGER
);
```

![16](/401/screenshots/sql16.png)

## 17. Altering Tables

`ALTER TABLE` specify the data type of the column along with any potential table constraints and default values to be applied to both existing and new rows

```SQL
ALTER TABLE mytable
ADD column DataType OptionalTableConstraint 
    DEFAULT default_value;
```

`DROP` Remove columns

```SQL
ALTER TABLE mytable
DROP column_to_be_deleted;
```

`RENAME` Rename table

```SQL
ALTER TABLE mytable
RENAME TO new_table_name;
```

![17](/401/screenshots/sql17.png)

## 18. Dropping Tables

`DROP TABLE` removes table schema from database, entire table removed

```SQL
DROP TABLE IF EXISTS mytable;
```

![18](/401/screenshots/sql18.png)

📔[Back to Main Page](../README.md)
