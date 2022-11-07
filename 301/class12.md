# 12. CRUD

## Why this is important:

Understanding status codes will help us understand the process of what our backend server is doing. They help us see how the server is working. 

1. In your own words, describe what each group of status code represents:
    - 100’s = Informational, request received and the server will trh to comply with transmission

    - 200’s = SUCCESS! client request accepted.

    - 300’s = Redirection. Requested resource is unavailable at request point.

    - 400’s = Client error. invalid requests. 

    - 500’s = Server error codes.

2. What is a status code 202?

    - 202 Accepted: used with asynchronous processing. Request accepted, still processing.

3. What is a status code 308?

    - Permanent Redirect, requested url deprecated, client needs to use another url.

4. What code would you use if an update didn’t return data to a client?

    - 204 No content

5. What code would you use if a resource used to exist but no longer does?
    
    - 410 Gone

6. What is the ‘Forbidden’ status code?

     - 403

## Build A REST API With Node.js, Express, & MongoDB

1. Why do we need to pull our MongoDB database string out of our server and put it into our .env?

    - to keep our DB key safe

2. What is middleware?
What does app.use(express.json()) do?

    - allows our server to accept json files as a body.
    
3. What does the /:id mean in a route?

    - this defines a parameter that must be met.

4. What is the difference between PUT and PATCH?

    - patch allows us to update based on what the user passes in. 

5. How do you make a default value in a schema?

    - by defining invidual properties and adding Date.now

6. What does a 500 error status code mean?

    - server error

7. What is the difference between a status 200 and a status 201?

    - 200: Request received and understood. 201: request is successful, source is created.

## Things I want to know more about:

I want to do more work on the backend. 

### Resources

[Status Codes Based On REST Methods](https://www.moesif.com/blog/technical/api-design/Which-HTTP-Status-Code-To-Use-For-Every-CRUD-App/)

[Build A REST API With Node.js, Express, & MongoDB](https://www.youtube.com/channel/UCFbNIlppjAuEX4znoulh0Cw)