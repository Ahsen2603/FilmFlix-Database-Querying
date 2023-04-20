from connect import * 
from readfilms import *

# cursor.execute(
#     """
# CREATE TABLE "tblfilms" (
# 	"filmID"	INTEGER NOT NULL UNIQUE,
# 	"Title"	TEXT,
# 	"Year_Released"	INTEGER NOT NULL UNIQUE, 
# 	"Rating"	TEXT,
#  	"Duration"	INTEGER,
# 	"Genre"	TEXT,
# 	PRIMARY KEY("filmID" AUTOINCREMENT)
# )"""
# )

# cursor.execute(
#     """
# INSERT INTO tblfilms(filmID, Title, Year_Released, Rating, Duration, Genre)
# VALUES(
# Home from the Hill,1960,18,150,Drama|Romance
# Christiane F.,1981,18,138,Drama
# Fair Game,1995,15,91,Drama|Thriller
# Friday the 13th Part VIII: Jason Takes Manhattan,1989,18,100,Horror
# Time Without Pity,1957,PG,85,Crime|Drama|Mystery
# Seven Angry Men,1955,U,90,Drama|Western
# Bad News Bears Go to Japan,1978,PG,91,Comedy
# The Invitation,2022,15,105,Drama|Horror|Thriller
# Art & Copy,2009,PG,89,Documentary
# Taken 3,2014,12A,108,Crime|Drama|Mystery|Romance|Thriller
# Master of Ballantrae,1953,PG,90,Adventure
# Nirvana,1997,18,113,Action|Sci-Fi
# The Big Trail,1930,U,125,Adventure|Romance|Western
# Jailhouse Rock,1957,18,96,Crime|Drama|Musical|Romance
# Russian Doll,2005,15,125,Comedy|Romance)
# )"""

# )

# creating a list of items


multiple_columns = [()]

cursor.executemany("INSERT INTO tblfilms VALUES (?,?,?,?,?,?)", multiple_columns)
conn.commit()