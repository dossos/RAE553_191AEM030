import   sqlite3  # import  SQLite  database which pytthon self-existent

connection  =  sqlite3.connect( 'data.db')   # establish connection with database

cursor  =  connection. cursor ( )  #  create  cursor  object



create_table  =  "CREATE  TABLE  IF  NOT  EXISTS  users  (id  INTEGER  PRIMARY  KEY ,  username  text  ,  password  text )" # define users id as interger in colums
cursor.execute (create_table)   #  execute  SQL commands which we deifination


create_table  =  "CREATE  TABLE  IF  NOT  EXISTS  items  (name  text  PRIMARY  KEY ,  price  real )" # define items  resources for each fields 
cursor.execute (create_table)

# cursor.execute ( "INSERT  INTO  items  VALUES  ( ' test'  ,   10.99)")    
# excecute insert specific item for test and use # symbol to change  unneeded codes to annotation after finished

connection.commit ( )   #  save our changes
connection.close ( )  # close database  connection after finished