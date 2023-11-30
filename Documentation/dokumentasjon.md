# Dokumentasjon 
når jeg startet prosjektet laget jeg et nytt [GitHub-repo](https://github.com/Eduard2303/Python-Password-Manager) for å administrere alle de forskjellige versjonene av programmet mitt. Jeg startet med å lage en .json-fil med noen dummy-passord slik at jeg kan begynne å jobbe med søkefunksjonen.

## Passwords.json
```json
{
	"Google": {

		"email/Username": "USER@gmail.com",

		"password": "x4d%d+*%4cdGIE30e"

	},



	"Youtube": {

		"email/Username": "youtubeuser@gmail.com",

		"password": "l=6c8MwC>syS6,9Ldbn`]"



	},

	"Twitter": {

		"email/Username": "Twitteruser",

		"password": "mFYG:m:PIoBJ:!Oz5-<60"

	},



	"Reddit": {

		"email/Username": "Reddit_user1",

		"password": "nW993|U|rd=|TwR=5*D8v"

	}

}
```

Jeg har også laget 2 python-filer. En main.py for kjøring av porgrammet og en functions.py for å lage funksjoner og importere dem i main.py filen.


## functions.py
Jeg startet i functions.py-filen ved å lage funksjonen som søker etter passord.

Dette er den første versjonen av koden før testing.
```python
def findpassword(database,website):
    import json

  

    with open(database, 'r') as file: #Åpner .json file i lese modus.

        data = json.load(file) #leser filen og lagrer i data variblen.

  

    if website in data: #Sjekker om siden blir er i data basen.

        username = data[website]["email/Username"] #Hvis ja lagre passord og brukernavn.

        password = data[website]["password"]

  

        return username, password #Retrun brukernavn og passord.

  

    else:

        return "No website with this name." #hvis ikke return feil melding


findpassword("password.json", "Google")
```

  
Fikk en file not found error fordi jeg skrev filnavnet feil. 
```python
FileNotFoundError: [Errno 2] No such file or directory: 'password.json'
```

Riktig kode
```python
findpassword("Passwords.json", "Google")
```

Etter det fik jeg en JSONdecode error.
```python
JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)`
```

  
så jeg tenkte at jeg sannsynligvis ikke søkte gjennom filen riktig. 
Jeg begynte å forenkle koden min for å se hva som fungerte og ikke fungerte.

Jeg lagde en test for å se om jeg kunne lese filen.
```python
import json
with open("Passwords.json", 'r') as file: #Åpner .json file i lese modus.
		
	data = json.load(file) #leser filen og lagrer i data variblen.
  
		if "Google" in data:
			print("true")
		else:
			print("false")
```
Konsollen returnerer True.

Jeg prøvde å skrive ut passordet og brukernavnet.
```python
import json

  

with open("Passwords.json", 'r') as file: 


        data = json.load(file) 
        

        username = data["Google"]["email/Username"] 

        password = data["Google"]["password"]
        
        print(username,password)
```

Dette fungerte så jeg la til funksjonen.

```python
import json



def findpassword(database,website):



    with open(database, 'r') as file: #Åpner .json file i lese modus.

        data = json.load(file) #leser filen og lagrer i data variblen.

  

    #if website in data: #Sjekker om siden blir er i data basen.

        username = data[website]["email/Username"] #Hvis ja lagre passord og brukernavn.

        password = data[website]["password"]

  

        return username, password #Retrun brukernavn og passord.

  

    #else:

    #   return "No website with this name." #hvis ikke return feil melding.

  

findpassword("Passwords.json", "Google")
```

Outputen var tom, og jeg fant ut at det var fordi jeg ikke skrev ut noe funksjonen.

```python
print(findpassword("Passwords.json", "Google"))
```
Nå skrev den ut.

Til slutt testet jeg funksjonen og fikk den til å fungere.
```python
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

print(findpassword("Passwords.json", "Google"))

print(findpassword("Passwords.json", "website"))
```

Output
```Terminal
('USER@gmail.com', 'x4d%d+*%4cdGIE30e')
False
```

Nå skal jeg lage add-funksjonen i den samme filen.

```python
def addnew(database):

    with open(database, 'r') as file: #Åpner .json file i lese modus.

        data = json.load(file)

    website = str(input("What website do u want to add? ")) # Spør bruker input hviken nettside.

    if website == "":

        return "Website can not be empty"
        
    if website in data: #Hvis finnes aleredre send error.
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
```

Dette er den første versjonen av legg til funksjonen. Jeg har laget en kopi av .json-filen slik at jeg kan erstatte den hvis programmet sletter den.

I will run Jeg skal kjøre denne koden:
```python
print(addnew("Passwords.json"))
```
  Så jeg kan se i outputen om det vil fullføre eller ikke.

Når jeg blir bedt om input, setter jeg nettstedet som "Google"
Outputen var False fordi den netsider finnes allerede, dette forteller meg at testen fungerer.

Nå prøver jeg å legge til et innlegg. Når jeg ble bedt om det, skrev jeg inn website, bruker1 og password0101. Den outputtet True, og i .json filen så jeg at den la til innlegget.
```json
{
    
   "website": {
        "email/Username": "bruker1",

        "password": "password0101"
}
```
  
Jeg prøvde også å legge inn et tomt nettsted for å teste den andre sjekken. Og den returnerte "Passordet kan ikke være tomt". 

Nå skal jeg lage fjern innlegg-funksjon.

```python
def removeenry(database):

    with open(database, "r") as file: #Opner fil og lagere dataen i var data.

        data = json.load(file)

    entry = str(input("What entry do u want to remove? ")) #Tar input hvilken innlegg skal slettes.  

  

    if entry in data:   #Hvis finnes slett.

        del data[entry]

    else:   #Else return error

        return False

    with open(database, "w") as file:  #lagrer ny fil som ertater den andre.

        json.dump(data, file, indent=4)    

        return True
```

Jeg syntes det var for enkelt å slette en fil, så jeg la til en bekreftelse.

```python
    if entry in data:   #Hvis finnes slett.

        confirm=str(input(f"{entry} was found in {database} are u sure you want to delete this entry? y/n")) #Brukeren må konfirmere at de vil slette.

        if confirm == "y" or confirm == "Y":

            del data[entry]

        else:

            return "Aborted by User"
```

Jeg laget en liten funksjon for å liste opp alle innleggene i manageren.

```python
def listall(database):

	with open(database, "r") as file: # Åpne fil og lagre data.

		data = json.load(file)

  

	print("These are all the entrys in the file:")

	for entry in data: #Skrive ut hvert innlegg

		print (entry)
```

Jeg har laget også funksjonen for å generere tilfeldige passord.

```python
def randomapass(lenght):

	characters = string.ascii_letters + string.digits + string.punctuation # Lage en liste med alle bokstaver tall og symboler.

	password = "".join(secrets.choice(characters) for _ in range(lenght)) # Velger en tilfeldig bokstav fra characters og legger den til password.

	return password
```

og jeg oppdaterte koden i addentry.

```python
password = str(input("What do you want the password to be? or chose type r for random password")) #Input passord og brukenavn.



if password == 'r':

	lenght = int(input("Choose lenght"))

	password = randomapass(lenght)
```

Det er alle funksjonene, og jeg kan gå videre til hovedfilen.
## main.py

Jeg importerte først funksjonene fra fuctions.py-filen. Og setter noen variabler.
```python
from fuctions import * #Impotere funksjonene fra fuctions.py
choice = "" #Valg variablen
database = "Passwords.json" #Data base path.
```

Og så skrev jeg en while-løkke for å se etter hvert alternativ. Jeg brukte funksjonen "choice.lower()" for å gjøre om store bokstaver til små bokstaver. Dette gjør sånn at jeg trenger bare en sjekke.

```python 
while choice.lower() != "e": # Loop til choice er "e"

    choice = str(input("Chose an option.\n\nList Password(L)\nView entry(V)\nNew entry(N)\nRemove entry(R)\nExit(E)\n")) #Skirver ut de forskjelige funksjoene.
    

    if  choice.lower() == "l":
		pass
		
    elif choice.lower() == "v":
        pass
    
    elif choice.lower() == "n":
		pass
		
    elif choice.lower() == "r": 
	    pass


    elif choice.lower() == "e": #Hvis choice er "e" bare pass over og loopen slutter.
        pass
    
    else: #Hvis ingen funksjon blir valgt.
        print("Option not found")
```
  
Listall funksjonen trenger ikke å returnere noe bra skriv ut.
```python
if  choice.lower() == "l":
	print(listall(database))
	pause()
```

  
Jeg har laget også en ny funksjon kalt pause(). Den pauser bare koden slik at brukeren kan lese outputen og be dem om å trykke enter for å fortsette.

```python
def pause():
	print("Press Enter to continue...")
	input()
```

nå tar vi noen input og søker etter nettsiden ved hjelp av funksjonen. Hvis vi får False, skriver vi "Ikke funnet" ellers hvis vi får True, så skriver vi ut passord og brukernavn.

```python
elif choice.lower() == "v":

		website = str(input("What website do you want to view. "))

		if findpassword(database, website) == False: #Sjekker om den returnrer False. Dette btyr innlegg finnes ikke.

			print("Entry not found")

			pause() #Pause fuksjon.

		else: #Hvis innlegg finnes skriver ut.

			username, password  = findpassword(database, website)

			print(f"Website:{website}\nUsername:{username}\nPassword:{password}")

			pause()
```

Samme her vi sjekker for feil hvis det er ingen feil skriver vi ut det.

```python
elif choice.lower() == "n":

		output = addentry(database) #Kaller funk    

		if output == False: # Hvis False skriv ut error.

			print("Entry can not have the same name.")

			pause()
            
			elif output == True: # Hvis True så har innlegg blit laget.

			print("Entry added successfully")

			pause()

		else:
        
			print(output) #Ellers skriv ut annen error.

		pause()
```


Og det samme for det siste alternativet.
```python
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
```
