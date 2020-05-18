from  flask_restful  import  Resource , reqparse # import restful resource and reqparse function
from  flask_jwt import  jwt_required   # require a valid JWT  token  to be present in the request
import  sqlite3  #  import  database


class  Item(Resource) : #  define items  resources
        TABLE_NAME  =  ' items' # set database table equal to items resources

        parser  =  reqparse.RequestParser ()
        parser .add_argument  ( 'price',     # add an argument  price to be parsed, define type as string and field also is required 
               type=float,
               required=True,
               help='This field cannot  be  left  blank!'
        )

        def  post  (self  ,  name):   #  use POST method send 'name' item source, this is critical step also should be the first step 
                if  self.find_by_name (name):
                        return  {"message":  "An  item  with  name  '{}'  already  exists" . format (name)}
            #  define   duplicate 'name' return  reminder
                data  =  Item.parser.parse_args ( )  #  parse all arguments from provided request and return the results as data
                item  =  {'name' :  name ,  'price' :  data['price']}

                try:  #   insert  name and  price  relevent information into  items resources
                        Item. insert (item)
                except:
                        return  { "message" :  "An error  occurred  inserting  the  item."} , 500

                return  item,  201
    
        @classmethod
        def  insert  (cls ,  item):  #  define insert  method in tables
                connection  =  sqlite3.connect ( 'data.db')
                cursor  =  connection.cursor ( )

                query  =  "INSERT  INTO  {table}  VALUES  (?,?) "  .  format (table = cls .TABLE_NAME)  # use SQL command insert  item infromation including name and price
                cursor.execute ( query, (item['name'], item ['price']))
                connection.commit()
                connection.close ()
                return  { 'message': 'Item Added'}

        @jwt_required ( )  #   use GET method read request  item resource mainly about name which stored in database,   use jwt token authenticate
        def  get ( self ,   name ):
                item  =  self  . find_by_name (name)
                if  item: 
                        return  item
                return  {'message' :  'Item  not  found'} ,404

        @classmethod
        def  find_by_name (cls, name):  #  define serching by name  method in tables as we defined before
                connection  =  sqlite3.connect ('data.db')
                cursor  =  connection.cursor  ( )

                query  =  "SELECT  *  FROM  {table}  WHERE  name=?" . format ( table  = cls. TABLE_NAME)
                result  =  cursor.execute (query,  (name ,)) # return a single  row
                row  =  result.fetchone ( )  # if row match with name then  return name and price use only row data
                connection.close ( )

                if  row: 
                         return  { 'item' :  {'name' :  row[0],  'price':  row[1]}}

        @jwt_required ( ) #  use  PUT method update items resources by 'name',  here also need jwt token authenticate
        def  put  (self , name) :
                data  =  Item.parser.parse_args ( )
                item  =  self .find_by_name (name)
                updated_item  =  { 'name' :  name,  'price' : data['price']}   
                if  item  is  None:
                       try:
                               Item. insert (updated_item)  #  insert  items  update   
                       except:
                               return  { 'message' :  "An  error  occurred  updating  the  item. "}
                else:
                        try:
                               Item. update (updated_item)  
                        except:
                               raise  # display  trigger  exception
                               return  { 'message' :  "An  error  occurred  updating  the  item. "}  #  return  reminder message
                return   updated_item #  finish  update items resources

        @classmethod
        def  update  ( cls,  item): #  after PUT method updation , use updata method update database
                connection  =  sqlite3.connect ('data.db')
                cursor =  connection.cursor ( )

                query  =  "UPDATE  {table}  SET  price=?  WHERE  name=?" . format  ( table=cls.TABLE_NAME) 
                cursor.execute (query ,  (item  ['price'],  item ['name']))

                connection.commit  ( )
                connection.close ( )

        @jwt_required ( ) # we also can delete items resources by delete method 
        def  delete (self , name ):
                connection  =  sqlite3.connect ('data.db')
                cursor  =  connection.cursor  ( )

                query  =  "DELETE  FROM  {table}  WHERE  name=?" . format (table = self.TABLE_NAME) #  use sql command delete items resource by  'name'
                cursor.execute (query,  (name ,))
                connection.commit ( )
                connection.close ( )

                return  { 'message'  :  'Item  deleted'}
