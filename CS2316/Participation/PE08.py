import pymysql, sys
from pprint import pprint
import getpass

'''
This participation exercise uses the RODEODRIVE database that contains three tables,
the stores, employees, and the product table.

Utilize the following steps to execute the RodeoDrive.sql file after downloading
it from the PE08 folder.

    1. Open MySQL Workbench
    2. Log into your local server
    3. On the top left, click on File > Open SQL Script... > RodeoDrive.sql
    4. Once the .sql file is opened in MySQL Workbench, click on the lightning icon
       to execute the script
    5. After the script has been executed, click on the "Schemas" tab in the Navigator
       area on the left
    6. Click on the refresh button in the Navigator tab, and the "rodeodrive" database
       should now be present

The RodeoDrive.sql file has three tables:

+---------------+
|    tables     |
+---------------+
| stores        |
| employees     |
| product       |
+---------------+

The stores table has the following attributes -store_id, name,
num_employees, revenue, and rating.

+-----------------+--------------+
|   COLUMN_NAME   |  DATA_TYPE   |
+-----------------+--------------+
| store_id        | int          |
| name            | varchar      |
| num_employees   | int          |
| total_revenue   | decimal      |
| rating          | int          |
+-----------------+--------------+

The employees table has the following attributes - employee_id, name,
store_id, and salary.

+-----------------+--------------+
|   COLUMN_NAME   |  DATA_TYPE   |
+-----------------+--------------+
| employee_id     | int          |
| name            | varchar      |
| store_id        | int          |
| salary          | int          |
+-----------------+--------------+

The products table has the following attributes - name, store_id, and price.

+-----------------+--------------+
|   COLUMN_NAME   |  DATA_TYPE   |
+-----------------+--------------+
| name            | varchar      |
| store_id        | int          |
| price           | decimal      |
+-----------------+--------------+
'''

"""
NOTE on %s:
The % sign in pymysql acts a placeholder for an input value. Think of this as
a SQL specific f-string. Given an input parameter, use %s as a placeholder within your query.
When the request is made to the sql server, the cursor and an equivalent amount of parameters
must be passed to fill all spots where an %s has been placed.
For furthur clarification, look at the prewritten function calls at the bottom
of this file.
"""

'''
Write a query that finds the
    [employee_id, name, store_id, salary] of employees
    who earn [less than or equal to] 30,000.
'''
def query1(cursor):
    '''Fill in the query'''
    query = 'SELECT * FROM employees WHERE salary <= 30000;'
    cursor.execute(query)
    result = cursor.fetchall()
    return result

'''
Write a query that finds the
    [name, num_employees, and total_revenue]
    of [stores whose name begins with a 'C']
    AND [have a total revenue between 5,000,000 and 8,000,000]
'''
def query2(cursor):
    '''Fill in the query'''
    query = 'SELECT name,num_employees,total_revenue FROM stores WHERE name LIKE "c%" and total_revenue > 5000000 and total_revenue < 8000000'
    cursor.execute(query)
    result = cursor.fetchall()
    return result

'''
Write a query that finds the
    [name, total_revenue]
    of [the top 5 stores based on their total_revenue]
'''
def query3(cursor):
    '''Fill in the query'''
    query = 'SELECT name,total_revenue FROM stores ORDER BY total_revenue DESC LIMIT 5;'
    cursor.execute(query)
    result = cursor.fetchall()
    return result

'''
Write a query that finds the
    [store id, total sum of employee salaries as 'Total Salary']
    [where the sum of salaries is greater than 50,000]
    [grouped by the store id]

Hint: This will involve a join of two tables where one table will provide
      the store_id and the other will provide the employee salaries.
'''
def query4(cursor):
    '''Fill in the query'''
    query = 'SELECT store_id,sum(salary) FROM stores JOIN employees USING (store_id) GROUP BY store_id HAVING sum(salary)>50000';
    cursor.execute(query)
    result = cursor.fetchall()
    return result

'''
Write a query that finds the
    [store name, total count of all products at that store]
    [where the store_id is greater than the min_id]
    [grouped by the store name]
    [having the total count is greater than min_items]
'''
def query5(cursor, min_id, min_items):
    '''Fill in the query'''
    query = 'SELECT stores.store_id, COUNT(stores.store_id) FROM stores JOIN products ON products.store_id = stores.store_id WHERE stores.store_id >"%s" GROUP BY stores.store_id HAVING COUNT(stores.store_id)>"%s"'
    cursor.execute(query, (min_id, min_items,))
    result = cursor.fetchall()
    return result

def main():

    ################## Insert MySQL Server password when running file via command prompt if applicable ##################

    user_password = getpass.getpass('\n# Enter your MySQL Server password. If no password is set up, press ENTER: ')
    
    try:
        connection = pymysql.connect(host = 'localhost',
                                     user = 'root',
                                     password = user_password,
                                     db = 'RodeoDrive',
                                     charset = "utf8mb4",
                                     cursorclass = pymysql.cursors.Cursor)

        print('\n# Connection with database successfully established.\n')

    except Exception as e:
        sys.exit(f"\n# Error occured.\n# {e}")

    ########################### Test Cases ###########################
    with connection.cursor() as cursor:
        pass
        
        # Query 1
        # print(">>> query1(cursor)")
        # pprint(query1(cursor))

        # Query 2
        # print(">>> query2(cursor)")
        # pprint(query2(cursor))

        # Query 3
        # print(">>> query3(cursor)")
        # pprint(query3(cursor))

        # Query 4
        # print(">>> query4(cursor)")
        # pprint(query4(cursor))

        # Query 5
        # print(">>> query5(cursor, 2, 1)")
        # pprint(query5(cursor, 2, 1))



if __name__ == '__main__':
    main()
