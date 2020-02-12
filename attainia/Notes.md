I wasn't sure if you wanted the rest api to serve the json from a file or to save it in the 
database so I did both.

The first view in the views file loads the data from the file as json, and filters 
it as requested and returns it to the caller as json.

For the user models, I created a user model with fields corresponding to the fields in the
json file. I then loaded the file to the local sqldb with the following commands:


