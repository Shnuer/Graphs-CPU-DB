# import the mysql client for python
import pymysql
# Create a connection object
dbServerName    = "127.0.0.1"
dbUser          = "root"
dbPassword      = "1"
dbName          = "test"
charSet         = "utf8mb4"
cusrorType      = pymysql.cursors.DictCursor

 # need autocommit for adding data to table
connectionObject   = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword,
                                     db=dbName, charset=charSet,cursorclass=cusrorType, autocommit=True)
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
            
            sqlQuery            = 'describe ' + values + ';'
            cursorObject.execute(sqlQuery)

            data = cursorObject.fetchall()
            print(data)
            for val_1 in data:
                print(val_1['Field'])
 
    # add data to table    
    sqlQuery            = "INSERT INTO Employed (id, LastName, FirstName, DepartmentCode) VALUES (1, 'John', 'James', 255);"

    print(sqlQuery)    
    cursorObject.execute(sqlQuery)


    sqlQuery            = "INSERT INTO Employed (id, LastName, FirstName, DepartmentCode) VALUES (2, 'NotJohn', 'NotJames', 256);"

    print(sqlQuery)    
    cursorObject.execute(sqlQuery)

    sqlQuery            = "SELECT * FROM Employed;"

    print(sqlQuery)    
    cursorObject.execute(sqlQuery)

    print(cursorObject.fetchall())
    # # get table
    # sqlQuery            = "show tables"   
    # cursorObject.execute(sqlQuery)
    # print('Im here')

    # #Fetch all the rows
    # rows                = cursorObject.fetchall()
    # print(type(rows))
    # for row in rows:
    #     for key, values in row.items():
    #         print(values)
            
    #         sqlQuery            = 'describe ' + values + ';'
    #         cursorObject.execute(sqlQuery)

    #         data = cursorObject.fetchall()
    #         print(data)
    #         for val_1 in data:
    #             print(val_1['Field'])

    # # Execute the sqlQuery
    # cursorObject.execute(sqlQuery)


    print()
    print('Ok Im get all table')


    # sqlQuery            = "DROP TABLE Employed"   
    # cursorObject.execute(sqlQuery)
    print("Wow")

except Exception as e:
    print("Exeception occured:{}".format(e))

finally:
    connectionObject.close()