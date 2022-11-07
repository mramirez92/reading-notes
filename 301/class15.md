# 15. Auth0

## Why is this important:

To protect sensitive user information, we can implement authentication.

## Auth0

1. What is OAuth?
    - OAuth is an open-standard authorization protocol or framework that describes how unrelated servers and services can safely allow authenticated access to their assets without actually sharing the initial, related, single logon credential.

2. Give an example of what using OAuth would look like.

    - Using another website like google to login to a website. 

3. How does OAuth work? What are the steps that it takes to authenticate the user?

    1. initial website connects to secondary website to provide users verified identity. 
    2. second website generates one-time toke and one time secret. 
    3. first site gives this token and secret to the initiating user’s client software.
    4. client software presents req. token to their authentication provider. 

4. What is OpenID?
    - Authenticates user, while Oauth is machines authenticating each other. 

## Authorization and Authentication Flows

1. What is the difference between authorization and authentication?

    - Authentication authenticates users and authorization defines what resources can be accessed.

2. What is Authorization Code Flow?

    - Authorization code is exchanged for a token. User is authenticated by a second website, who gives a code to user. This along with client id are sent to auth0 authorization server for verification.Auth0 server responds with an ID token and Access token with which an API call can be made. 

3. What is Authorization Code Flow with Proof Key for Code Exchange (PKCE)?
    - similar to code flow, except a code challenge and verifier are sent back to Auth0 authentication server. 

4. What is Implicit Flow with Form Post?
    
    - web app requests and obtains tokens through the front channel, without the need for secrets or extra backend calls. With this method, you don’t need to obtain, maintain, use, and protect a secret in your application

5. What is Client Credentials Flow?

    - app is authenticated/authorized rather than the user. 

6. What is Device Authorization Flow?

    - device asks the user to go to a link on their computer or smartphone and authorize the device. This avoids a poor user experience for devices that do not have an easy way to enter text.

7. What is Resource Owner Password Flow?

    - users provide credentials (username and password), typically using an interactive form.

## Things I want to know more about:

I want to implement Auth0 in my future projects.

## Resources

[What is OAuth](https://www.csoonline.com/article/3216404/what-is-oauth-how-the-open-authorization-framework-works.html)

[Authorization and Authentication flows](https://auth0.com/docs/flows)