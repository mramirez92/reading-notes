# 11. Mongo DB and Mongoose

## Why this is important:

Working with databases can help us expand the amount of data our web apps can process.

## SQL vs NoSQL

|NoSQL | SQL |
|------|------|
|data stored in key value pairs, graph, or wide column stores|data store in table databases|
|dynamic schema for unstructured data| predefined schema|
|queries focused on collection of documents| uses structured query language|
|DB: MongoDB, BigTable, Redis| DB: MySql, Oracle, Sqlite|
|Not for high load transactional apps| Handles high load transactional apps easy|

1. What kind of data is a good fit for an SQL database?
    - data that needs to be structured,  maybe an online store.
2. What kind of data is a good fit a NoSQL database?
    - data that can be stored with key value pairs, like a movie db
3. Which type of database is best for hierarchical data storage?
    - MongoDB
4. Which type of database is best for scalability?
    - SQL

-----
### SQL
SQL is not a DB its a language.

`SELECT id, name, price, FROM products`

SQL schema must be the same across the board. All records in table have to adhere to that schema.

- data distributed across multiple tables
- horizontal scaling, data can't be split across multiple servers.


|ID|Name|Price| Description|
|-----|-----|-----|-----|
|1| shirt | 19.99| graphic shirt with wolf|
|2 | socks | 7.99| pigeon print socks |

### MongoDB
Databases are split into "collections"; collections contain documents, they don't have to use the same schema. Flexible,new data can be added later. No relations.

- vertical scaling has limits as far as computing power.
- data can be split because of how data is stored in collections.
- schema-less, can be less reliable when you are expecting certain data.
- keep constantly queried data in one collection.
- great for (simple) read & write requests.

1. What does SQL stand for?
    - Structured Query Language
2. What is a relational database?
    - data in database have connections to multiple tables, data can merge together.
3. What type of structure does a relational database work with?
    - tables
4. What is a ‘schema’?
    - fields, how data is going to be stored in DB
5. What is a NoSQL database?
    - Collection that contains documents
6. How does it work?
    - Data is store in collections that contain documents, with key and value pairs. Less relational merging allows for faster queries.
7. What is inside of a MongoDB database?
    - database and collections
8. Which is more flexible - SQL or MongoDB? and why
    - MongoDb allows us to store data without following strict schema, data can reside in the same document without the same fields as its counterparts.
9. What is the disadvantage of a NoSQL database?
    - Because noSql has little or no relations, data is duplicated. When modifications are needed we will need to change data in all of the documents.

## Things I want to know more about:
I just want to start working with mongo.     

## References

[SQL vs NoSQL](https://www.thegeekstuff.com/2014/01/sql-vs-nosql-db/?utm_source=tuicool)

[SQL vs NoSQL or MySQL vs MongoDB](https://www.youtube.com/watch?v=ZS_kXvOeQ5Y)

📔[Back to Main Page](../README.md)