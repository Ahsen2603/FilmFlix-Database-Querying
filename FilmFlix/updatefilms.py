from connect import *
from readfilms import *
import time

def update():
    "filmID, Title, Year_Released, Rating, Duration, Genre, "
    
    idfield = input("Enter the filmID, of the record to be updated: ")
    
    fieldName = input("Enter (filmID, Title, Year_Released, Rating, Duration, Genre) as field name ")
    
    fieldValue = input(f"Enter the value for the {fieldName} field: ")
    
    print(fieldValue)
    
    fieldValue = "'" + fieldValue + "'"
    
    print(fieldValue)
    
    cursor.execute(f"UPDATE film SET {fieldName} = {fieldValue} WHERE SongID = {idfield}")
    conn.commit() # make the change permanent
    print(f"Record {idfield} updated in the film table")
    time.sleep(3)# delay for three seconds

    # call/invoke the read film function from the rea film.py file 
    read()
if __name__ =="__main__":
    update()