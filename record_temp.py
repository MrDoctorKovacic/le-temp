import time
import temp_humid
import MySQLdb

db = MySQLdb.connect("XXX","XXX","XXX","XXX")
cursor = db.cursor()

insert_timestamp = time.time()
temp_array = temp_humid.get_temp()
sql = """INSERT INTO log_temp(timestamp,
         temp, humid)
         VALUES (%d, %d, %d)""" % \
	 (insert_timestamp, temp_array[0], temp_array[1])
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()

print(temp_humid.get_temp())
