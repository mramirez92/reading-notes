## User Stories

Music Discovery – As a user, I want to be able to discover new music inspired by images. 

- Feature Tasks
  - Users will have multiple images to choose from 
  - Based on user selection, a track will be rendered 
  - Track information will be displayed 

- Acceptance Tests
  - Users will have the ability to choose an image and receive a track corresponding to the image description/qualities. 
  - Track information will be displayed after clicking. 

Song info – As a user, I want to be able to see the title and artist of that song so that I can obtain artist information.

- Feature Tasks
  - Track will display info: artist, track name, album.
- Acceptance Tests
  - Successfully retrieve data from Spotify API and display appropriate information in component

Saved Recommendations – As a user, I want to be able to save my recommendations and return them later.

- Feature Tasks
  - Users can log in with Auth0
  - Users can opt to choose what they want to save
  - Users can go back and see what tracks they discovered (and possibly the image associated)
- Acceptance Tests
  - Ensure that users can successfully login/logout
  - Ensure that users can successfully retrieve the tracks they've discovered

User Interface – As a user, I want to interact with an easy-to-read interface

- Feature Tasks
  - Bootstrap components will be implemented
  - Fonts and sizes will be readable
  - Instructions  explaining functionality will be displayed somewhere on page 
- Acceptance Tasks
  - Bootstrap components will be displayed using flex.
  - Font sizes will be readable and contrast with the background color/image. 
  - Instructions will be displayed on the main page  

Image Choice – As a user I want to be able to have random multiple image options to choose from.

- Feature Tasks
  - Random images will be displayed 
  - Selection renders track based on image
- Acceptance Tests
  - Track is relatively related to the image.
  - The image does not always give us the same track.

## Software Requirements:

### Vision

- What is the vision of this product? - To create an intersection of visual arts and music 

- What pain point does this project solve? - Creates a new avenue for targeted song recommendation

- Why should we care about your product? - You should care because new methods of content curation will lead to fresher recommendations and thus increased engagement

### Scope (In/Out)

- IN (What will it do?): 
  - The web app will provide images for the user to choose from
  - Based on image selection, the web app will render a track that will have the image's descriptive properties match some part of the track title. 
  - Possibly allow users to discover new music based on simple images. 

- OUT (What will it not do?):

  - Become a mobile app.
  - Create new music
  - Save previously seen images to local storage or cache.

## Minimum Viable Product vs Stretch Goals

### What will your MVP functionality be?

  - The MVP functionality of this application is to take a description of an image from the Unsplash API and using any/all of the words in the description to get a random song on Spotify.

### What are your stretch goals?

- Integrate a Computer Vision API such as Google Cloud Vision API to take in any random image provided, generate labels and/or description to open up the possible images a user could use.
Instead of generating a single song, generate a whole playlist.

### What stretch goals are you going to aim for?

- Integrate the Computer Vision API to expand possible images used.

### Functional Requirements

- A user can select an image from Unsplash and get a song
- A user can login and save the song they got 
- A user can access all of the songs that they had generated

## Data Flow

1. Web app displays random images from Unsplash API. 
2. Front-end(user) makes an image selection, that selection is sent to our local server. 
3. Local server processes the GET request and communicates with Spotify API using schema defined. 
4. Spotify API will respond with data matching request. 
5. Local server will send the requested data to the front end to store in state.  
6. Front end will use a function to randomly choose a song to display. 
7. Front end will display the received data to the user.

Non-Functional Requirements
Protects user’s Spotify account data. Implements Auth0 in such a way so that relevant data is displayed to the user and other user data is not
Interface is clear and the user is able to interact with it intuitively and effectively.