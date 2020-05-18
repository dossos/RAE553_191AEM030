from  werkzeug.security  import   safe_str_cmp # compare strings in somewhat constant time
from   user  import  User  #  import  user data


def  authenticate(username,  password):  
    user  =  User.find_by_username (username) #  according our user.py defination,  we can use user information to here and authenticate
    if  user  and  safe_str_cmp (user .password   , password  ): #  we get safe string after authenticate and compare string if same retrun true  otherwise false
        return user  # now we get correctly user and could be logged in


def  identity (payload) :
        user_id  =   payload [  'identity'  ] #  extract  user id from payload  and return a specific user
        return User .find_by_id (user_id)  #  retrieve  users by  user  ID which we definited in user file