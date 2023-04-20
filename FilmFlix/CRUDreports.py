from connect import *
import time

# CRUD commands/functions

#~ Prints all films in Table


   #good 
def read():
    cursor.execute("SELECT * FROM tblfilm") 
    row = cursor.fetchall()
    for record in row:
        print(record)
       
   # good    
#~ print Genre
def printGenre(genre):
    cursor.execute("SELECT * FROM tblfilm WHERE Genre = '" + genre + "'")
    row = cursor.fetchall()
    for record in cursor.fetchall():
        print(record)

# print year

def printYear(year):
    cursor.execute("SELECT * FROM tblfilm WHERE Year_Release = '"+ year + "'")
    row = cursor.fetchall()
    for record in cursor.fetchall():
        print(record)
    
def printRating(rating):
    cursor.execute("SELECT * FROM tblfilm WHERE Rating = '"+ rating + "'")
    row = cursor.fetchall()
    for record in cursor.fetchall():
        print (record)

if __name__=="__main__":
    read()        