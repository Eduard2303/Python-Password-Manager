import json

def findpassword(database,website):
    with open(database, 'r') as file: #Åpner .json file i lese modus.
        data = json.load(file) #leser filen og lagrer i data variblen.

    if website in data: #Sjekker om siden blir er i data basen.
        username = data[website]["email/Username"] #Hvis ja lagre passord og brukernavn.
        password = data[website]["password"] 
        return username, password #Retrun brukernavn og passord.
    else:
        return False #hvis ikke return feil melding.

def addentry(database):
    with open(database, 'r') as file: #Åpner .json file i lese modus.
        data = json.load(file)
         
    website = str(input("What website do u want to add? ")) # Spør bruker input hviken nettside.

    if website == "":
        return "Password can not be empty"


    check = findpassword(database,website) #Bruker finn fuksjonen for å skjekke om det finnes.
    if check != False: # Hvis check ikke er False betyr det at inn legge finnes.
        return False # returnerer false sånn at vi kan se at det failet.

    else:
        password = str(input("What do you want the password to be? ")) #Input passord og brukenavn.
        username = str(input("What do u want the username to be? "))

# Lager innleget som med alle variablene.
        new_entry = {                      
        website: {
            "email/Username": username,
            "password": password
        }
    }
        data.update(new_entry) #legger til innlegget til den andre dataen.

    #Skriver ut ny .json file som erstater den andre.
    with open(database, "w") as file:
        json.dump(data, file, indent=4)
    
    return True #Sender melding at innlegget har blit lagdt til.



def removeenry(database):
    with open(database, "r") as file:
        
        data = json.load(file)
    
    entry = str(input("What entry do u want to remove? "))

    