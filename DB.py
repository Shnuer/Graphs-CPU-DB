# import the mysql client for python
import pymysql
# Create a connection object
dbServerName    = "127.0.0.1"
dbUser          = "root"
dbPassword      = "1"
dbName          = "test"
charSet         = "utf8mb4"
cusrorType      = pymysql.cursors.DictCursor

 
connectionObject   = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword,
                                     db=dbName, charset=charSet,cursorclass=cusrorType)
try:                                   
    # Create a cursor object
    cursorObject        = connectionObject.cursor()                                     

    # SQL query string
    sqlQuery            = "CREATE TABLE Employed(id int, LastName varchar(32), FirstName varchar(32), DepartmentCode int)"    
    
    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)
    # SQL query string
    sqlQuery            = "show tables"   

    # Execute the sqlQuery
    cursorObject.execute(sqlQuery)
    print('Im here')

    #Fetch all the rows
    rows                = cursorObject.fetchall()
    print(type(rows))
    for row in rows:
        for key, values in row.items():
            print(values)
            val = 'describe ' + values + ';'
            print(val)
            # sqlQuery            = 'describe %s;' % values
            # cursorObject.execute(sqlQuery)
            
 
        
        


    print()
    print('Ok Im get all table')


    sqlQuery            = "DROP TABLE Employed"   
    cursorObject.execute(sqlQuery)
    print("Wow")

except Exception as e:
    print("Exeception occured:{}".format(e))

finally:
    connectionObject.close()