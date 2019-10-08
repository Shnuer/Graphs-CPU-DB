# import the mysql client for python
import pymysql
import cpu_read

table_header = []
separator = ', '

def commandAddDataToDB(current_core_load):
    """ Create command for added new data in table.
        Input: current core load in list
        Output: command for MySQL
    """
    
    string_constant_add_value_table = 'INSERT INTO Core_value'
    
    # list with headers to string
    headers_list_to_string = separator.join(table_header)
    # list with value CPU to string
    val_for_db = separator.join(str(x) for x in current_core_load)

    #create command for add new data
    command = string_constant_add_value_table + '(%s)' % headers_list_to_string + ' VALUES (%s);' % val_for_db
    return command


def commandCreateForMysql():
    """Function return Two Value's:
        
        1) String with command for create table
        #2) List with headers
        """

    #get list with value percent CPU 
    list_with_core = cpu_read.get_percentage_CPU()

    # maybe change default name table and type headers
    string_constant_create_table = 'CREATE TABLE Core_value'
    type_val = ' float(2)'
    
    # fill in the list in which would be table header: 'id, 1_core, 2_core, ... n_core'
    for i in range(len(list_with_core)):
        num_core = i + 1
        table_header.append('%d_core' % num_core)

    # create new list for adding type header
    list_with_val_for_create_command = []

    # fill the new list with headers types 
    for val_in_list in range(len(table_header)):
        list_with_val_for_create_command.append(table_header[val_in_list] + type_val)

    list_with_val_for_create_command.append('id int NOT NULL AUTO_INCREMENT')
    list_with_val_for_create_command.append('time TIMESTAMP(5)')
    list_with_val_for_create_command.append('PRIMARY KEY (id)')

    # list with headers types to string
    string_with_param_for_create_table = separator.join(list_with_val_for_create_command)

    # create command for MySQL
    command_for_create_table = string_constant_create_table + '(%s);' % string_with_param_for_create_table

    return command_for_create_table







# Create a connection object
dbServerName    = "127.0.0.1"
dbUser          = "root"
dbPassword      = ""
dbName          = "test"
charSet         = "utf8mb4"
cusrorType      = pymysql.cursors.DictCursor

 
connectionObject   = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword,
                                     db=dbName, charset=charSet,cursorclass=cusrorType, autocommit=True)
cursorObject = connectionObject.cursor()

def createTable():
    try:
        sqlQuery = commandCreateForMysql()
        cursorObject.execute(sqlQuery)
        print('Im create?')

    except Exception as e:
        print("Exeception occured:{}".format(e))
        print('Im do not create')

    # finally:
    #     connectionObject.close()


def updateTable(current_core_load):

    try:
        sqlQuery = commandAddDataToDB(current_core_load)
        cursorObject.execute(sqlQuery)
        # print('Im update?')

    except Exception as e:
        print("Exeception occured:{}".format(e))
        # print('Im do not update')

def deleteTable():

    # sqlQuery = 'DROP TABLE Core_value'
    # cursorObject.execute(sqlQuery)
    connectionObject.close()

    # finally:
    #     connectionObject.close()






