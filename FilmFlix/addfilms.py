from connect import *   # This is a module which calls on connect which understands the inputs of 
from readfilms import * # This importsd the previous file made for a specific function
import time # The module for the time library


def insertFilms(): #defining the function/procedure of insert films
    #create an empty list 
    films= [] # films empty list place holder for list
    
    #; ask for user input title, Year_Realeased, Rating, Duration and Genre
    
    Title = input ("Enter Film Tiltle: ")   #user input for Title
    Year_released = input ("Enter film year_Released: ")  #user input for Artist
    Rating = input ("Enter film rating: ")  #user input for Artist
    Duration = input ("Enter film duration(mins): ")  #user input for Artist
    Genre = input ("Enter film genre: ")    #user input for Genre
    
    # append data from the above inputs
    
    films.append(Title)  # adds the above input title to films = []
    films.append(Year_released) # adds the above input year_released to films = []
    films.append(Rating) # adds the above input rating to films = []
    films.append(Duration) # adds the above input duration to films = []
    films.append(Genre)  # adds the above input rating to films = []
    
    # or
    # films.extend([title, artist, genre])
    
    # Insert/add data from the films list into the database in the films table
    cursor.execute("INSERT INTO tblfilms(Title, Year_released, Rating, Duration, Genre) VALUES(?,?,?,?,?)", films) #? "INSERT INTO films() values()" we use '?' to avoid sql injection
    # cursor helps to point at a particular table or data earlier we made an alias for cursor = conn.cursor
    conn.commit() #make changes permanent
    time.sleep(3) # delay from calling the read file form the readfilms.py file
    read() # call read function readfilms.py file
    
if __name__ == "__main__": 
    insertFilms()



    
     
    