from  flask  import  Flask , request
from  flask_restful  import  Resource,  Api , reqparse
from  flask_jwt  import JWT,   jwt_required ,   current_identity

from  security  import   authenticate,  identity


app  =   Flask(__name__)
app.secret_key = 'Tianhua'
api   =  Api(app)


items  =  [ ]

class  Item(Resource) : 
    def  get (self,   name) :
        for  item in  items : 
            if  item[ 'name' ]  ==  name :
                        return  item
                        return {'item':  None}, 404

    def  post  (self  ,  name): 
                        data = request. get_json( )
                        item = {'name': name, 'price' : data ['price']}
                        items.append(item)
                        return  item,        201  


    def  put  ( self,    name ):
              parser  =  reqparse .  RequestParser (  )
              parser . add_argument  ( ' price'  ,
                    type  =  float  ,
                    required  =  True ,
                    help  =  'This  field  cannot  be  left  blank!'
               )
              data  =  parser . parse_args (  )
              print ( data['another']) ;
              item  =  next(filter (lambda x:    x['name']  ==   name,  items ),   None)
              if   item  is   None : 
                    item  =  {'name':  name,   'price':   data['price']}
                    items . append(item)
              else :
                    item . update (data)
              return  item

class ItemList(Resource) :
    def  get(self):
                        return{'items' : items}

jwt  =  JWT (app,   authenticate,   identity)

@app .route ('/auth')
@jwt_required( )


def  auth ( ):
           return   '%s'   %    current_identity

if   __name__  == '__main__' : 

          api . add_resource ( Item,  '/item/<string:name>')
api . add_resource (ItemList,  '/items')

app. run (port=5000,  debug=True)