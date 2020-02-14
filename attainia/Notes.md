I wasn't sure if you wanted the rest api to serve the users from the json file or to save it in the 
database and then serve it so I did both.

The first view in the views file loads the data from the file as json, and filters 
it as requested and returns it to the caller as json.

Model
------
For the user model, I extended django's built in abstract user model and added the fields
corresponding to the fields in the json file. I then redid the built in UserForms
and added the new model to the admin interface. I made a copy of users.json and modified
it slightly so it could be loaded as a fixture. If it were a larger file I would have just
converted it to a csv in a terminal and loaded it into the database.

Testing
--------
For unit tests, I mostly focused on covering the views since the forms and model don't really have
any custom methods. I tested with the API Test Client since the views themselves are extremely simple
without much logic, judging their functionality based on their response. I used factory boy to 
create models for testing.


Obviously if this were a real application there are still a number of things that would need to be
done. A real project would have a set up to run test coverage tools, check for syntax errors etc.




