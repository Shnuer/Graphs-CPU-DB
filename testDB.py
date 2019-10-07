import cpu_read

type_variable_for_core = ' int'
list_with_column_table_of_contents = []
def commandCreateForMysql():
    """Function return Two Value's:
        
        1) String with command for create table
        2) List with all num core"""

    #get list with value percent CPU 
    list_with_core = cpu_read.get_percentage_CPU()

    # constant for create string mysql command
    string_with_command_mysql = 'CREATE TABLE Employed(id int'
    

    # a list in which there will be value with num core
    list_with_column_table_of_contents =[]

    for i in range(len(list_with_core)):
        num_core = i+1
        list_with_column_table_of_contents.append('%d_core'%num_core)
        string_with_command_mysql = string_with_command_mysql + ', ' + list_with_column_table_of_contents[i] + type_variable_for_core

    string_with_command_mysql = string_with_command_mysql+')'

    return string_with_command_mysql, list_with_column_table_of_contents

def commandAddDataToDB():
    pass


if __name__ == "__main__":

    string_comand_create, list_with_num_core = commandCreateForMysql()

    print(string_comand_create)
    print()
    print(list_with_num_core)