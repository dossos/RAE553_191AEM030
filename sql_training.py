import   sqlite3

connection   =   sqlite3.connect(  'data.db' )

cursor  =  connection.cursor ( )

create_table  =  "CREATE  TABLE  users  (id  int,  username  text,  password  text)"

cursor.execute ( create_table)

user  =  (1,  'tianhua',  '12345') 
insert_query  =  "INSERT  INTO  users  VALUES  (?,  ?,  ?)"
print(user)
user  =  (2,  'eva',  '123456')
insert_query  =  "INSERT  INTO  users  VALUES  (?,  ?,  ?)"
print(user)
user  =  (3,  'bob',  'asdf')
insert_query  =  "INSERT  INTO  users  VALUES  (?,  ?,  ?)"
print(user)
user  =  (4,  'john',  'cvbn')
insert_query  =  "INSERT  INTO  users  VALUES  (?,  ?,  ?)"
print(user)
user  =  (5,  'constance',  '987654')
insert_query  =  "INSERT  INTO  users  VALUES  (?,  ?,  ?)"
cursor.execute ( insert_query, user)
print(user)

connection.commit ()
connection.close ( )