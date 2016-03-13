
#-----Statement of Authorship----------------------------------------#
#
#  By submitting this task the signatories below agree that it
#  represents our own work and that we both contributed to it.  We
#  are aware of the University rule that a student must not
#  act in a manner which constitutes academic dishonesty as stated
#  and explained in QUT's Manual of Policies and Procedures,
#  Section C/5.3 "Academic Integrity" and Section E/2.1 "Student
#  Code of Conduct".
#
#  First student's no: PUT 1ST STUDENT'S NUMBER HERE
#  First student's name: PUT 1ST STUDENT'S NAME HERE
#  Portfolio contribution: PUT 1ST STUDENT'S PERCENTAGE CONTRIBUTION HERE
#
#  Second student's no: PUT 2ND STUDENT'S NUMBER HERE
#  Second student's name: PUT 2ND STUDENT'S NAME HERE
#  Portfolio contribution: PUT 2ND STUDENT'S PERCENTAGE CONTRIBUTION HERE
#
#  Contribution percentages refer to the whole portfolio, not just this
#  task.  Percentage contributions should sum to 100%.  A 50/50 split is
#  NOT necessarily expected.  The percentages will not affect your marks
#  except in EXTREME cases.
#
#--------------------------------------------------------------------#


#-----Task Description-----------------------------------------------#
#
#  DATA STATISTICS
#
#  In this task you will use a Python program to construct and
#  interrogate an SQL database to produce statistics for
#  a large amount of textual data.
#
#  You are required to write the following four functions:
#
#  1) populate_table
#  This function reads data from a file specified by the parameter
#  and enters the data into a table which has the same name as the
#  file, and then returns the number of rows inserted.
#
#  2) best_and_worst
#  Given the name of a make of car, this function prints the make and
#  the minimum and maximum overall rating given to cars of this make
#  by the owners.  If no such make of car exists the function must
#  print an appropriate message.
#
#  3) most_expensive
#  This function prints the make, model, price and overall rating of
#  the most expensive cars in the database, one car per line.
#  Its parameter is a number specifying how many lines to print.
#
#  4) average_ratings
#  Given a make of car, this function prints the average overall
#  rating awarded to each model of this make.  If no such make of
#  car exists the function must print an appropriate message.
#
#  In each case use the unit tests below to determine the layout of
#  the result to be printed.  Take particular note of the sequence
#  in which the results must be printed as this may influence the
#  ordering you specify in your SQL query.
#
#--------------------------------------------------------------------#


#-----Acceptance Tests-----------------------------------------------#
#
#  This section contains the unit tests that your program must
#  pass.  You may not change anything in this section.  NB: When
#  your program is marked the following tests will be used as
#  well as some additional tests (not provided) to ensure your
#  solution works for other cases.
#
"""
---------- Populating the database tables

>>> int(populate_table("car_details")) # Test 1 (updated)
3119

>>> int(populate_table("car_ratings")) # Test 2 (updated)
5504

---------- Best and worst overall ratings 

>>> best_and_worst('TOYOTA') # Test 3
TOYOTA (1-5)

>>> best_and_worst('VOLVO') # Test 4
VOLVO (2-5)

>>> best_and_worst('LEXUS') # Test 5
LEXUS (4-5)

>>> best_and_worst('CADILLAC') # Test 6
CADILLAC (4-4)

>>> best_and_worst('LIGHTBURN') # Test 7
No such make of car!

---------- Most expensive cars

>>> most_expensive(1) # Test 8
FERRARI 575M: $551000, Overall rating 4

>>> most_expensive(4) # Test 9
FERRARI 575M: $551000, Overall rating 4
FERRARI 599: $551000, Overall rating 5
MERCEDES-BENZ E55: $225600, Overall rating 5
JAGUAR XJR: $178000, Overall rating 5

>>> most_expensive(15) # Test 10
FERRARI 575M: $551000, Overall rating 4
FERRARI 599: $551000, Overall rating 5
MERCEDES-BENZ E55: $225600, Overall rating 5
JAGUAR XJR: $178000, Overall rating 5
MERCEDES-BENZ E500: $153900, Overall rating 1
BMW 7: $145900, Overall rating 4
BMW 7: $136500, Overall rating 4
JAGUAR XJ8: $126500, Overall rating 3
JAGUAR S TYPE: $124500, Overall rating 5
MERCEDES-BENZ 300: $124500, Overall rating 4
LEXUS LX470: $119100, Overall rating 4
MERCEDES-BENZ CLK230: $112200, Overall rating 5
MERCEDES-BENZ CLK320: $112200, Overall rating 4
MERCEDES-BENZ E280: $112200, Overall rating 5
MERCEDES-BENZ E280: $112200, Overall rating 3
 
>>> most_expensive(0) # Test 11 (produces no output)

---------- Average ratings of the cars

>>> average_ratings('HOLDEN') # Test 12 (updated)
MONARO 4.8
TORANA 4.6
VIVA 4.4
PREMIER 4.4
COMBO 4.3
CRUZE 4.3
CALAIS 4.3
KINGSWOOD 4.3
BERLINA 4.2
JACKAROO 4.2
NOVA 4.1
ASTRA 4.1
BARINA 4.0
COMMODORE 4.0
VECTRA V6 4.0
ADVENTRA 3.9
CAPTIVA 3.9
VECTRA 3.8
CREWMAN 3.8
CAMIRA 3.7
EPICA 3.7
FRONTERA 3.6
RODEO 3.6
CALIBRA 3.6

>>> average_ratings('KIA') # Test 13 (updated)
OPTIMA 5.0
PREGIO 5.0
GRAND CARNIVAL 4.9
MAGENTIS 4.4
SORENTO 4.3
CERATO 4.3
K2700 4.0
RIO 3.8
SPORTAGE 3.6
CARNIVAL 3.5
SPECTRA 3.3
MENTOR 3.0

>>> average_ratings('DAIHATSU') # Test 14
COPEN 5.0
MIRA 5.0
APPLAUSE 4.4
TERIOS 4.2
CHARADE 4.0
SIRION 4.0
FEROZA 3.8
PYZAR 3.7

>>> average_ratings('LIGHTBURN') # Test 15
No such make of car!

""" 
#
#--------------------------------------------------------------------#



#-----Students' Solution---------------------------------------------#
#
#  Complete the task by filling in the template below.


# Get the MySQL-Python functions:
import MySQLdb

##    # Alternative for Mac users:
##    import mysql.connector
##    MySQLdb = mysql.connector


##### PUT YOUR DATA STATISTICS FUNCTIONS HERE

##### Populate Table Function #####
def populate_table (files):
     try:
## open connection to db
          connection = MySQLdb.connect(host = "localhost", user = "root",passwd = "", db = "car_reviews")
## place cursor
          cursor = connection.cursor()
     except Exception:
          print 'Database Error! Check db and password'
          return 0
## Clear existing Data
     cursor.execute('TRUNCATE '+files)
## Open text file
     text = file(files+'.txt','r')
## subfunction to build sql row insert statements
     def inserttext(content):
          # Break at Columns
          row = content.strip().split('\t')
          # Start Statement
          buildrow = 'INSERT INTO ' + files + " VALUES ('"
          # add column values
          for column in range(len(row)):
               buildrow = buildrow + row[column] + "', '"
          # finish and return sql statement
          buildrow = buildrow[:len(buildrow)-3] + ")"
          return buildrow
## Start Counter
     total=0
## Make and run insert functions for each row
     for line in text:
          sql = inserttext(line)
          cursor.execute(sql)
## Add to total rows inserted
          total = total + int(cursor.rowcount)
## Safe Disconnect from database
     connection.commit()
     connection.close()
## Return number of rows modified
     return total



##### Best and worst Function #####
def best_and_worst(make):
     try:
## open connection to db
          connection = MySQLdb.connect(host = "localhost", user = "root",passwd = "", db = "car_reviews")
## place cursor
          cursor = connection.cursor()
     except Exception:
          print 'Database Error! Check db and password'
          return
## Make sql statement
     sql = "SELECT make, MIN(overallRating), MAX(overallRating) FROM car_ratings Inner JOIN car_details ON car_ratings.carID=car_details.carID WHERE make='"+make+"' GROUP BY make;"
## Run sql statement
     cursor.execute(sql)
## Get results                       Note: return in form (('make', 1L, 5L),)
     values = cursor.fetchall()
## Safe Disconnect from database
     connection.close()
     try:
## Convert results to desired format
          result= values[0][0]+' (' + str(int(values[0][1]))+'-'+ str(int(values[0][2]))+')'
          print result
     except Exception:
          print 'No such make of car!'



##### Most Expensive #####
def most_expensive(number):
     try:
## open connection to db
          connection = MySQLdb.connect(host = "localhost", user = "root",passwd = "", db = "car_reviews")
## place cursor
          cursor = connection.cursor()
     except Exception:
          print 'Database Error! Check db and password'
          return
     sql='SELECT DISTINCT make, model, price, overallRating FROM car_ratings INNER JOIN car_details ON car_ratings.carID=car_details.carID ORDER BY price desc, make asc, model asc, overallRating desc;'
     cursor.execute(sql)
     values = cursor.fetchall()
     connection.close()
     try:
          for index in range (number):
               print str(values[index][0])+' '+str(values[index][1])+': $'+str(values[index][2])+', Overall rating '+str(values[index][3])
     except Exception:
          print 'Range Error'
# MERCEDES-BENZ CLK320: $112200, Overall rating 4

#####
def average_ratings(make):
     try:
## open connection to db
          connection = MySQLdb.connect(host = "localhost", user = "root",passwd = "", db = "car_reviews")
## place cursor
          cursor = connection.cursor()
     except Exception:
          print 'Database Error! Check db and password'
          return
     print 'finish code here'

##     SELECT make, model, ROUND(avg(overallRating),1)
##     FROM car_ratings INNER JOIN car_details
##     ON car_ratings.carID=car_details.carID
##     GROUP BY model       






#
#--------------------------------------------------------------------#



#-----Automatic Testing----------------------------------------------#
#
#  The following code will automatically run the acceptance tests
#  when the program is "run".  Do not change anything in this
#  section.  If you want to prevent the tests from running, comment
#  out the code below, but ensure that the code is uncommented when
#  you submit your program.
#
if __name__ == "__main__":
     from doctest import testmod
     testmod(verbose=True)   
#
#--------------------------------------------------------------------#

