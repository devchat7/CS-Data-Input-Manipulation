import pymysql
import getpass
# no other imports allowed

# first, run the provided schema.sql file to create the PE09 database.
#
# for the following functions,
#   - use the connection in the parameters to create a cursor
#   - use the cursor, to execute SQL statements
#   - call connection.commit() to save changes you make to the database
#
# reference the pymysql handout for more details on using pymysql

########### QUICK TIP FOR DEBUGGING ##############
"""
While testing your code via the command line,
you will have to repeatedly type in your SQL password.
To bypass this,
comment out the user_password line, requesting your
password via the command line. Then, hardcode your password
as a string in the creation of the variable password.
For example, if my password was 'password', my connection variable would look like...
connection = pymysql.connect(host = 'localhost',
                                 user = 'root',
                                 password = 'password',
                                 db = 'PE09',
                                 charset = "utf8mb4",
                                 cursorclass=pymysql.cursors.Cursor)
"""


def reset_database(connection):
    """
    Creates two tables, characters and actor. If the tables already exist,
    drop them first. The tables should contain the following columns containing
    the associated data types. You do not need to insert any data for this
    question.

    characters -- table layout (5 columns):
        characterID          : int AUTO_INCREMENT PRIMARY KEY
        name                 : varchar(255)
        skill                : varchar(255)
        age                  : int
        actorID              : int

    actor -- table layout (4 columns):
        actorID              : int AUTO_INCREMENT PRIMARY KEY
        name                 : varchar(255)
        numEpisodes          : int
        numCharacters        : int


    returns: None
    """
    with connection.cursor() as cursor:
        cursor.execute ('drop table if exists characters;')
        cursor.execute ('drop table if exists actor;')
        cursor.execute ('create table characters (characterID int primary key AUTO_INCREMENT, name varchar(255), skill varchar(255), age int, actorID int);')
        cursor.execute ('create table actor (actorID int primary key AUTO_INCREMENT, name varchar(255), numEpisodes int, numCharacters int);')
        connection.commit()


def insert_character(connection, name, skill, age, actorID):
    """
    Insert a new character into the character table using the parameters given.

    Hint:
    You don't need to input the characterID column, but you MUST use %s for the other columns.

    returns: None
    """
    with connection.cursor() as cursor:
        query = 'INSERT INTO characters (name, skill, age, actorID) VALUES (%s, %s, %s, %s)'
        cursor.execute(query, (name, skill, age, actorID))
        connection.commit()


def update_num_Character(connection):
    """
    In the actor table, for each actor, update the total number of characters in
    the characters table that belong to the actor.

    returns: None
    """

    with connection.cursor() as cursor:
        cursor.execute ('Select actorID, count(actorID) FROM characters GROUP BY actorID;')
        fetched = cursor.fetchall()
        for x in fetched:
            cursor.execute('update actor set numCharacters = %s WHERE actorID = %s;', (x[1],x[0]))
        connection.commit() 


def delete_actor(connection, num_episodes):
    """
    Given the parameter `num_episodes` (int), delete all the actors that have their number
    of episodes to be less than or equal to `num_episodes`, as well as all their
    corresponding characters.
    Make sure to commit your changes at the very end.

    Hint:
    It is best to first write a query to find all of the actorIDs that have number
    of episodes to be less than or equal to `num_episodes`.
    Once you have the actorIDs, you can delete those corresponding records in both
    the `actor` and `characters` tables.

    Returns: None
    """
    cursor = connection.cursor()
    query = 'SELECT * FROM actor WHERE numEpisodes <= %s;'
    cursor.execute(query, num_episodes)
    fetched = cursor.fetchall()
    for x in fetched:
        cursor.execute('delete FROM actor WHERE actorID = %s', (x[0],))
        cursor.execute('delete FROM characters WHERE actorID = %s', (x[0],))
    connection.commit()


def main():
    user_password = getpass.getpass('\n# Enter your MySQL Server password: ')

    connection = pymysql.connect(host = 'localhost',
                                 user = 'root',
                                 password = "Streamwood7",
                                 db = 'PE09',
                                 charset = "utf8mb4",
                                 cursorclass = pymysql.cursors.Cursor)


    ##################### reset_database test case #####################
    # Uncomment out all lines of code below to run this test case
    # To ensure this ran properly, open my WorkBench, refresh your schemas, and
    # you should see a schema titled PE09. Click the drop down on PE09 tables,
    # and you should see two tables, actors and characters.

    #reset_database(connection)
    #reset_database(connection) # should not error when called twice
    ##################### reset_database test case #####################


    ##################### insert_character test case #####################
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO actor (name, numEpisodes, numCharacters) VALUES ('Jonathon Bailey', 17,0)")
        cursor.execute("INSERT INTO actor (name, numEpisodes, numCharacters) VALUES ('Phoebe Dynevor', 12,0)")
        cursor.execute("INSERT INTO actor (name, numEpisodes, numCharacters) VALUES ('Simone Ashley', 8,0)")
        cursor.execute("INSERT INTO actor (name, numEpisodes, numCharacters) VALUES ('Nicola Coughlan', 17,0)")
        cursor.execute("INSERT INTO actor (name, numEpisodes,numCharacters) VALUES ('Rege-Jean Page', 8,0)")
    #Uncomment out all lines of code below to run this test case

    print('\n>>> insert_character(connection,name,skill, age, actor_id)')
    insert_character(connection, "Duke of Hastings", "Banter", 26, 5)
    # insert_character(connection, "Lady Whistledown", "Secrecy", 19, 4)
    # insert_character(connection, "Penelope Featherington", "Eavesdropping", 19, 4)
    # insert_character(connection, "Daphne Bridgerton", "Diamonds", 20, 2)
    # insert_character(connection, 'Anthony Bridgerton', 'Brooding', 24, 1)
    # insert_character(connection, 'Kate Sharma', 'Girlbossing', 24, 3)
    # print('=========== Updated Actor Table ===========')
    # with connection.cursor() as cursor:
    #     cursor.execute("SELECT * FROM actor")
    #     for row in cursor.fetchall():
    #         print(row)
    ##################### insert_character test case #####################


    ##################### update_num_Character test case #########################
    # Uncomment out all lines of code below to run this test case

    print('\n>>> update_num_Character(connection)')
    # update_num_Character(connection)
    # print('=========== Updated Actor Table ===========')
    # with connection.cursor() as cursor:
    #     cursor.execute("SELECT * FROM actor")
    #     for row in cursor.fetchall():
    #         print(row)
    ##################### update_num_Character test case #########################




    ##################### delete_actor test case #####################
    # Uncomment out all lines of code below to run this test case

    print('\n>>> delete_actor(connection, 12)')
    # delete_actor(connection, 12)
    # with connection.cursor() as cursor:
    #     print('=========== Updated Actor Table ===========')
    #     cursor.execute("SELECT * FROM actor")
    #     for row in cursor.fetchall():
    #         print(row)

    #     print('\n======== Updated Characters Table =========')
    #     cursor.execute("SELECT * FROM characters")
    #     for row in cursor.fetchall():
    #         print(row)

    ##################### delete_actor test case #####################


if __name__ == "__main__":
    main()
