# 8. REST

## Why this is important:

Creating a backend that connects our frontend successfully is important. It's needs to be done in an efficient and clear manner.

-----

Representational State Transfer (REST) is an architectural style for building distributed systems based on hypermedia.
Although  REST API's use HTTP as their application protocol, REST is an independent protocol.

- REST APIs are designed around resources, which are any kind of object, data, or service that can be accessed by the client.
- Resources contain a URI (unique resource identifier)
        - `https://adventure-works.com/orders/1`
        - based on nouns (resource) and not verbs (operations of resource)

- GET:  retrieves representation of resource at URI, HTTP status code 200 (OK)
- POST: creates new resource at URI, HTTP status code 201 (Created)
-PUT: partial update of resource; HTTP status code 201 (Created), if method updates an existing resource, it returns either 200 (OK) or 204 (No Content)
- DELETE: removes resource at specified URI, HTTP status code 204 (No Content), if resource not found returns HTTP 404 (Not Found).

1. What does REST stand for?

    - Representational State Transfer (REST)

2. REST APIs are designed around a resources.

3. What is an identifier of a resource? Give an example.

    -  "order" in this url: `https://catssupplies.com/order`

4. What are the most common HTTP verbs?

    - GET, POST, PUT, PATCH, and DELETE.

5. What should the URIs be based on?

    - they should be based on nouns(resource)

6. `https://catssupplies.com/orders/`

7. What does it mean to have a ‘chatty’ web API? Is this a good or a bad thing?
    - Chatty servers are a bad thing. They send large amounts of small resources, instead of sending like data in a bigger resource.

8- 11:

- GET: retrieves representation of resource at URI.
- POST: creates new resource at URI.
- PUT: creates/replaces resources at URI.
- PATCH: partial update of resource.
- DELETE: removes resource at specified UR!

-----

## Things I want to know more about:

I want to know how to write better URI'

-----

## Resources

[API Design](https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design)

📔[Back to Main Page](../README.md)