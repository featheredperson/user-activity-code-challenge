I wasn't sure if you wanted the rest api to serve the users from the json file or to save it in the 
database and then serve it so I did both.

The first view in the views file loads the data from the file as json, and filters 
it as requested and returns it to the caller as json.

For the user models, I extended django's built in user model and added the fields
corresponding to the fields in the json file. I then redid the built in UserForms
and added the new model to the admin interface. I made a copy of users.json and modified
it slightly so it could be loaded as a fixture. 

For unit tests, I mostly focused on covering the views since the forms and model don't really have
any custom methods.


Obviously if this were a real application there are still a number of things that would need to be
done. A real project would have a set up to run test coverage tools, check for syntax errors etc.


