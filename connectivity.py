import mysql.connector as mycon
db= mycon.connect(
    host ='localhost', user= 'root', password= 'root' ,database='pydb'
)
print(db)
db_curr = db.cursor()
db_curr.execute('create table dmart(pro_no int, pro_name varchar(20),pro_loc varchar(8))')