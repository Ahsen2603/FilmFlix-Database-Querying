from connect import *
from readfilms import *
import time

def delete():
    " filmID, Title, Year_Released, Rating, Duration, Genre"
    idfield = input("Enter the filmID, of the record to be deleted: ")
    
    cursor.execute(f"DELETE FROM tblfilms WHERE filmID = {idfield}")
    conn.commit() #; Conn commit allows us to stay persistent in our changes
    
    time.sleep(3)# delay for three seconds

    # call/invoke the read films function from the readfilms.py file 
    read()
if __name__ =="__main__":
    delete()