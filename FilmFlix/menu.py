import readfilms
import addfilms
import updatefilms
import deletefilm
import CRUDreports
import time

#~ Create a function for the films menu

def menuOptions():
    options = 0    
    
    while options not in ["1","2","3","4","5","6"]: 
        print("Films Menu Options\nEnter:\n1. Print.\n2. Add.\n3. Update.\n4. Delete.\n5. Report.\n6. Exit")
        
        options = input("Enter an option from the films menu choices above: ")
        
        if options not in ["1","2","3","4","5","6"]: 
            print(f"{options} is not a valid choice! from the films menu")

def reportOptions():
    reportOpt = 0
    
    while reportOpt not in ["1","2","3","4","5"]: 
        print("Report Menu Options\n. Enter:\n1. Print All Films.\n2. Print a particular Genre.\n3. Print a particular Film Release Year.\n4. Exit to Main Menu")
    
        reportOpt = input("Enter an option from the films menu choices above: ")
        
        if reportOpt not in ["1","2","3","4","5"]: 
            print(f"{reportOpt} is not a valid choice! from the films menu")
            
        return reportOpt

mainProgram = True 
while mainProgram:
    mainMenu = menuOptions()
    if mainMenu == "1":
        readfilms.read()        
    
    elif mainMenu == "2":
        addfilms.insertfilms()        
    
    elif mainMenu == "3":
        updatefilms.update()        
    
    elif mainMenu == "4":
        deletefilm.delete()
    
    elif mainMenu == "5":
        
        reportOpt = True
        while reportOpt:
            reportOpt = reportOptions()
            if reportOptions() == "1":
                CRUDreports.read()
                
            elif reportOptions() == "2":
                genre = ""
                genre = input("Please enter the Genre: ")
                CRUDreports.printGenre(genre)
        
            elif reportOptions() == "3":
                year = ""
                year = input("Please enter the Genre: ")
                CRUDreports.printYear(year)
        
            elif reportOptions() == "4":
                rating = ""
                rating = input("Please enter the rating: ")
                CRUDreports.printRating()
            
            elif reportOptions() == "5":
                menuOptions()
        
            else:
                reportOpt = False
    
    
    else:
        mainProgram = False
    # time.sleep(3)
    input("Press the enter button to quit application")