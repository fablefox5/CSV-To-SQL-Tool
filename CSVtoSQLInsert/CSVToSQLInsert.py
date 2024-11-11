import csv
#Written in Python with version 3.9
#Written by Andrew Goldstein

def csv_to_sql_insert(csv_file, sql_file, table_name):
    # this line is for turning off the feature of SQL trying to check for substitution variables with the % sign
    sql_file.write('SET DEFINE OFF;\n')

    # file line prefix is used to make sure first line doesn't have a line break at the start, and the other lines do
    file_line_prefix = ''
    for line in csv_file:
        curr_line = csv_file.readline()
        # if current line has data, then read line and put the correct insert command format for the given table name
        if curr_line != '':
            csv_reader = csv.reader([curr_line], skipinitialspace=True)
            attrib_values = csv_reader.__next__()
            for i in range(8, 20):
                # adds an extra single quote if a string contains one already so that SQL doesn't have issues with it
                if attrib_values[i].find("'") != -1:
                    index = attrib_values[i].index("'")
                    attrib_values[i] = attrib_values[i][0:index] + "'" + attrib_values[i][index:len(attrib_values[i])]

            curr_command = (f"INSERT INTO {table_name} VALUES ("
                            f"{attrib_values[0]}, {attrib_values[1]}, {attrib_values[2]}, {attrib_values[3]}, "
                            f"{attrib_values[4]}, TO_DATE('{attrib_values[5]}', 'dd/mm/yyyy'), "
                            f"{attrib_values[6]}, '{attrib_values[8]}', '{attrib_values[11]}', "
                            f"'{attrib_values[13]}', '{attrib_values[14]}', '{attrib_values[15]}', "
                            f"'{attrib_values[16]}', '{attrib_values[17]}', '{attrib_values[18]}', "
                            f"'{attrib_values[19]}');"
                            )

            sql_file.write(file_line_prefix + curr_command)
            file_line_prefix = '\n'


def csv_to_sql_insert_bnb(csv_file, sql_file, table_name):
    # this line is for turning off the feature of SQL trying to check for substitution variables with the % sign
    sql_file.write('SET DEFINE OFF;\n')

    # file line prefix is used to make sure first line doesn't have a line break at the start, and the other lines do
    file_line_prefix = ''
    for line in csv_file:
        curr_line = csv_file.readline()
        # if current line has data, then read line and put the correct insert command format for the given table name
        if curr_line != '':
            csv_reader = csv.reader([curr_line], skipinitialspace=True)
            attrib_values = csv_reader.__next__()
            for i in range(8, 20):
                # adds an extra single quote if a string contains one already so that SQL doesn't have issues with it
                if attrib_values[i].find("'") != -1:
                    index = attrib_values[i].index("'")
                    attrib_values[i] = attrib_values[i][0:index] + "'" + attrib_values[i][index:len(attrib_values[i])]

            curr_command = (f"INSERT INTO {table_name} VALUES ("
                            f"{attrib_values[0]}, {attrib_values[1]}, {attrib_values[2]}, {attrib_values[3]}, "
                            f"{attrib_values[4]}, TO_DATE('{attrib_values[5]}', 'dd/mm/yyyy'), "
                            f"{attrib_values[6]}, '{attrib_values[8]}', '{attrib_values[11]}', "
                            f"'{attrib_values[13]}', '{attrib_values[14]}', '{attrib_values[15]}', "
                            f"'{attrib_values[16]}', '{attrib_values[17]}', '{attrib_values[18]}', "
                            f"'{attrib_values[19]}');"
                            )

            sql_file.write(file_line_prefix + curr_command)
            file_line_prefix = '\n'



def main():
    csv_file = open('Auto Sales data.csv')
    sql_file = open('ToyCarOrdersAndSales Insert Commands.sql', 'w')
    table_name = 'ToyCarOrdersAndSales'
    csv_to_sql_insert(csv_file, sql_file, table_name)
    csv_file.close()
    sql_file.close()

if '__main__' == __name__:
   main()