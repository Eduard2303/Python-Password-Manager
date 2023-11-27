import json #For databaser.
import secrets #For tilfeldige passord.
import string #For liste av bokstaver og tall.


def randomapass(lenght):
    characters = string.ascii_letters + string.digits + string.punctuation # Lage en liste med alle bokstaver tall og symboler.
    password = "".join(secrets.choice(characters) for _ in range(lenght)) # Velger en tilfeldig bokstav fra characters og legger den til password.
    return password


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
        return "Website can not be empty"
    if website in data: 
        return False 

    else:
        password = str(input("What do you want the password to be? or chose type r for random password ")) #Input passord og brukenavn.

        if password == 'r':
            lenght = int(input("Choose lenght "))
            password = randomapass(lenght)

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
        json.dump(data, file, indent=4) #Indent gjør databasen lettere å for menesker.
    
    return True #Sender melding at innlegget har blit lagdt til.



def removeenry(database):
    with open(database, "r") as file: #Opner fil og lagere dataen i var data.
        data = json.load(file)
    
    entry = str(input("What entry do u want to remove? ")) #Tar input hvilken inlegg skal slettes.  

    if entry in data:   #Hvis finnes slett.
        confirm=str(input(f"{entry} was found in {database} are u sure you want to delete this entry? y/n")) #Brukeren må konfirmere at de vil slette.
        
        if confirm == "y" or confirm == "Y": 
            del data[entry]
        else:
            return "Aborted by User"       

    else:   #Else return error
        return False
    
    with open(database, "w") as file:  #lagrer ny fil som ertater den andre.
        json.dump(data, file, indent=4)    
        return True
    
    
def listall(database):
    with open(database, "r") as file: # Åpne fil og lagre data.
        data = json.load(file)

    print("These are all the entrys in the file:")
    for entry in data: #Skrive ut hvert inlegg
        print (entry)
    print("Press Enter to continue...")
    input()


def pause(): #En liten fuksjon som jeg bruker i main scriptet for å pause koden.               
    print("Press Enter to continue...")
    input()
