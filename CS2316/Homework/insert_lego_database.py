################################################################################
# MAKE SURE YOUR DIRECTORY HAS THE FOLLOWING STRUCTURE                         #
# user -                                                                       #
#       ...                                                                    #
#          - HW08                                                              #
#                - data                                                        #
#                       - sets.csv                                             #
#                       - inventories.csv                                      #
#                       ...                                                    #
#                       - part_categories.csv                                  #
#                - HW08.py                                                     #
#                - insert_lego_database.pymysql                                #
#                - lego-database-schema.sql                                    #
################################################################################
import pymysql, csv, sys
def connect(args):
    global connection, cursor
    try:
        connection = pymysql.connect(host = 'localhost', user = args[0], password = args[1],\
                    db = 'lego', charset = 'utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()

    except Exception as e:
        print(f"\n\n################################################################################\n#\n# {args[0]} was denied access to lego database. The following exception occured...\n# {e}\n#\n################################################################################")

def read_data():
    with open("data/sets.csv", encoding = 'utf-8') as file:
        next(file)
        sets = [ (i[0], i[1], int(i[2]), int(i[3]), int(i[4])) for i in csv.reader(file)]

    with open("data/inventories.csv", encoding = 'utf-8') as file:
        next(file)
        inventories = [(int(i[0]), int(i[1]), i[2]) for i in csv.reader(file)]

    with open("data/inventory_sets.csv", encoding = 'utf-8') as file:
        next(file)
        inventory_sets = [ (int(i[0]), i[1], i[2]) for i in csv.reader(file)]

    with open("data/inventory_parts.csv", encoding = 'utf-8') as file:
        next(file)
        inventory_parts = [ (i, int(j[0]), j[1], int(j[2]), int(j[3]), \
                    True if j[4] == 't' else False) for i, j in enumerate(csv.reader(file))]

    with open("data/parts.csv", encoding = 'utf-8') as file:
        next(file)
        parts = [(i[0], i[1], int(i[2])) for i in csv.reader(file)]

    with open("data/colors.csv", encoding = 'utf-8') as file:
        next(file)
        colors = [(int(i[0]), i[1], i[2], True if i[3] == 't' else False) \
                 for i in csv.reader(file)]

    with open("data/themes.csv", encoding = 'utf-8') as file:
        next(file)
        themes = [ (int(i[0]), i[1], 0 if not i[2] else i[2]) for i in csv.reader(file)]

    with open("data/part_categories.csv", encoding = 'utf-8') as file:
        next(file)
        part_categories = [(int(i[0]), i[1]) for i in csv.reader(file)]
    return sets, inventories, inventory_sets, inventory_parts, parts, colors, themes, part_categories

def insert_data(data):
    sets, inventories, inventory_sets, inventory_parts, parts, colors, themes, part_categories = data

    query = "INSERT INTO colors VALUES (%s, %s, %s, %s);"
    cursor.executemany(query, colors)

    query = "INSERT INTO themes VALUES (%s, %s, %s);"
    cursor.executemany(query, themes)

    query = "INSERT INTO part_categories VALUES (%s, %s);"
    cursor.executemany(query, part_categories)

    query = "INSERT INTO sets VALUES (%s, %s, %s, %s, %s);"
    cursor.executemany(query, sets)

    query = "INSERT INTO inventories VALUES (%s, %s, %s);"
    cursor.executemany(query, inventories)

    query = "INSERT INTO inventory_sets VALUES (%s, %s, %s);"
    cursor.executemany(query, inventory_sets)

    query = "INSERT INTO parts VALUES (%s, %s, %s);"
    cursor.executemany(query, parts)

    query = "INSERT INTO inventory_parts VALUES (%s, %s, %s, %s, %s, %s);"
    cursor.executemany(query, inventory_parts)

    connection.commit()
    connection.close()

def main(args):
    connect(args)
    data = read_data()
    insert_data(data)
    print("\n##########################################################\n#\n#             Data Inserted Successfully.\n#\n##########################################################\n\n")

if __name__ == '__main__':
    main(sys.argv[1:])
