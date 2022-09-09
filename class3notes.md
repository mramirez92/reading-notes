### seeing your remote

Collaboration on Git projects requires us to interact with remote repositories. Multiple repositories can be worked on. We can push information and pull data from them.


commands:
- git remote:  allows us to view short names of all specified remote handles. 
- git remote -v: you can view all the remote URLs next to their corresponding short names
- git remote add *short name* *url*: creates new Git repository with a short name 

##### Fetching 

Fetching means pulling data you dont have from a remote project. 
Fetching only pulls new data from repository, but doesn't apply it to your local work.

- git fetch *remote-name*

#### Pushing

Push your cahnges upstream for sharing by using this command:
- git push *[remote name] *[branch-name]: Pushes committed changes from your local “master” branch upstream to the “origin” server.

📔[Back to Main Page](README.md)