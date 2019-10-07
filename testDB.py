import cpu_read

def commandCreateForMysql():
    """Function return Two Value's:
        
        1) String with command for create table
        2) List with headers"""

    #get list with value percent CPU 
    list_with_core = cpu_read.get_percentage_CPU()

    # maybe change default name table and type headers
    string_constant_create_table = 'CREATE TABLE Employed'
    separator = ', '
    type_val = ' int'

    table_header = []
    table_header.append('id')
    
    # fill in the list in which would be table header: 'id, 1_core, 2_core, ... n_core'
    for i in range(len(list_with_core)):
        num_core = i + 1
        table_header.append('%d_core' % num_core)

    # create new list for adding type header
    list_with_val_for_create_command = []

    # fill the new list with headers types 
    for val_in_list in range(len(table_header)):
        list_with_val_for_create_command.append(table_header[val_in_list] + type_val)

    # list with headers types to string
    string_with_param_for_create_table = separator.join(list_with_val_for_create_command)

    # create command for MySQL
    command_for_create_table = string_constant_create_table + '(%s)' % string_with_param_for_create_table

    return command_for_create_table, table_header
    


def commandAddDataToDB(table_header):
    string_constant_add_value_table = 'INSERT INTO Employed'
    print(string_constant_add_value_table)


if __name__ == "__main__":

    string_comand_create, list_with_num_core = commandCreateForMysql()

    print(string_comand_create)
    print()
    print(list_with_num_core)