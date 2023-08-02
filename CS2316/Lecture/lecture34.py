import pymysql
import getpass
mypass = getpass.getpass()
connection = pymysql.connect(host = 'localhost', user = 'root', password = mypass, 
      charset = 'utf8mb4', cursorclass = pymysql.cursors.DictCursor)
print(type(connection))

with connection.cursor() as cursor:
      statement = "show databases;"
      cursor.execute(statement)
      results = cursor.fetchall() 
      print(results)
      print(type(results)) # a list of dictionaries or tuple of tuples
      connection.commit()
      connection.close()
      
