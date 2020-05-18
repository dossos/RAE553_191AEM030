from  flask  import  Flask  #  three basic  required  environment  package including  flask, API interface and jwt token
from  flask_restful  import  Api
from  flask_jwt import JWT

from  security  import   authenticate,  identity  #  from  our created  security  file import  authenticate and identity  functions
from  user  import  UserRegister  #  import our created userregister resources
from  item  import  Item  # import our created items resources

app  =   Flask (__name__)  # create our application
app. secret_key  =   'tianhua' # set secret key to prevent from some users modifying contents
api =  Api (app)

jwt  =  JWT (app,  authenticate,  identity)

api . add_resource (Item, '/item/<string:name>') # pass multiple URLs to  the add_resource method on API object and each one will be routed to Item resource
api.  add_resource  (UserRegister, '/register')  #set endpoints with userregister resource in our user file

#here we cannot use ItemList resources and if we set them in item file, it will conflict with our table_name


app. run (port=5000,  debug=True)   