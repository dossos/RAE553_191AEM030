import   sqlite3  
from  flask_restful  import  Resource ,  reqparse  #  import  restful resource and reqparse function

class  UserRegister  (Resource):  #  define  user regitser  resource and sign in resource use their username  and password

    parser  =  reqparse.RequestParser ( )  #   enable  adding and parsing of multiple arguments in the context of a single request 
    parser. add_argument( 'username',   #  add an argument  username to be parsed, define string and field also is required 
            type=str,
            required=True,
            help="This field cannot be blank."
    )
    parser. add_argument( 'password',  #  add an argument  password to be parsed
            type=str,
            required=True,
            help="This field cannot be blank."
    )

    def  post  (self):  # use POST method create  and register user in database
            data  =  UserRegister. parser. parse_args ( )   #  parse all arguments from provided request and return the results as data

            if  User.find_by_username (data['username']): # if  use duplicate username register and return reminder
                  return  {"message":  "A  user  with  this  username  already  exists"},  400

            connection  =  sqlite3.connect ('data.db')
            cursor  =  connection.cursor ( )

            query  =  "INSERT  INTO  users  VALUES  (NULL,  ?,  ?)"  # insert user information which we created into database
            cursor.execute(query,  (data ['username'], data ['password'] ))

            connection.commit ( )
            connection.close ( )

            return  {"message":  "User  created  successfully ."} , 201


class    User:   #   define  user object  and set  properties
    def   __init__ (self,  _id,   username  ,  password):
               self.id  =  _id
               self.username  =  username
               self.password  =  password
    
    @classmethod   #   this is function modifer, the first parameter of classmethod is cls,compared with common instancemethod is self
    def   find_by_username (cls,  username): # define serching by username  method
              connection  =  sqlite3.connect( 'data.db') # connect to database
              cursor  =  connection.cursor ( )

              query  =  "SELECT  *  FROM  users  WHERE  username=?" #use SQL language find user by username
              result  =  cursor.execute(query,  (username, ))
              row  =  result . fetchone()  #return a single tuple, that is row, if there is no result , it returns None
              if  row:
                  user  =  cls (*row) #  rows are matched with  id ,  username  and  password
              else:
                  user  =  None
            
              connection.close( ) # close the connection with database
              return  user

    @classmethod
    def  find_by_id  (cls,  _id):
              connection  =  sqlite3.connect( 'data.db') 
              cursor  =  connection.cursor ( )

              query  =  "SELECT  *  FROM  users  WHERE  id=?" #use SQL language find user by id
              result  =  cursor.execute(query,  (_id, ))
              row  =  result . fetchone()
              if  row:
                  user  =  cls (*row)
              else:
                  user  =  None
            
              connection.close( )
              return  user