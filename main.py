from fuctions import * #Impotere funksjonene fra fuctions.py
choice = "" #Valg variablen
database = "Passwords.json" #Data base path.

# Welcome melding
print("Welcome to Python Password Manager")
pause()
print("\n\n\n\n\n\n\n\n")


while choice.lower() != "e": # Loop til choice er "e"

    choice = str(input("Chose an option.\n\nList Password(L)\nView entry(V)\nNew entry(N)\nRemove entry(R)\nExit(E)\n")) #Skirver ut de forskjelige funksjoene.
    

    if  choice.lower() == "l": #Kaller listall som skirver ut alle inlegg. (Bruker choice.lower for å sjekke både store og små bokstaver.)
        print(listall(database))

    #kaller view funk som viser et inlegg
    elif choice.lower() == "v":
        website = str(input("What website do you want to view. "))
        if findpassword(database, website) == False: #Sjekker om den returnrer False. Dette btyr inlegg finnes ikke.
            print("Entry not found")
            pause() #Pause fuksjon.
        else: #Hvis inlegg finnes skriver ut.
            username, password  = findpassword(database, website)
            print(f"Website:{website}\nUsername:{username}\nPassword:{password}")
            pause() 


    elif choice.lower() == "n":
        output = addentry(database) #Kaller funk    
        if output == False: # Hvis False skriv ut error.
            print("Entry can not have the same name.") 
            pause()

        elif output == True: # Hvis True så har inlegg blit laget.
            print("Entry added successfully")
            pause()
        else:
            print(output) #Ellers skriv ut annen error.
            pause()

    elif choice.lower() == "r": 
        output = removeenry(database) #Kaller funksjon
        if output == False: #print error og confirm melding.
            print("Entry dosent exist")
            pause()        
        elif output == True:
            print("Entry removed")
            pause()
        else:
            print(output)
            pause()


    elif choice.lower() == "e": # Hvis choice er "e" bare pass over og loopen slutter.
        pass
    
    else: #Hvis ingen funksjon blir valgt.
        print("Option not found")