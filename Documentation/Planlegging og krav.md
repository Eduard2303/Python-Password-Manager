# Python Password Manager
## idé

Lag en python-passordbehandler som lagrer passord og brukernavn i en json-fil. Brukeren kan hente passordet ved å søke etter nettstedets navn.
## Plan
 
### Mål og krav (fra mest til minst viktig).

Programmet vil lagre et brukernavn og et passord som kan hentes når noen søker etter nettstedet navn.

Programmet vil hente denne informasjonen fra en .json-databasefil. Dette er ikke sikkert fordi alt brukerpassordet i er lagret i uten kryptering i ren tekst.

Programmet vil ha en funksjon for å legge til flere inlegg i .json-filen der brukeren vil bli bedt om å angi en nettside navn, brukernavn og passord.

Brukeren vil også kunne fjerne en oppføring i databasen ved å velge slette alternativet.

Hvis brukeren ikke kan lage et passord, vil programmet ha muligheten til å generere et passord fra tilfeldige bokstaver, tall og symboler.
### computational thinking 

Her har jeg tatt kravene og brukt computational thinking for å lage algorithme i pseudo code.

**Mål: Hent ut passord og brukernavn fra nettsidens nettadresser.

Pseudokode:
 ```python
#Brukeren velger søkefunksjonen fra hovedmenyen
INPUT #Skriv inn navnet til nettstedet du vil logge på.
IF entry like INPUT in database
	RETURN entrie.password AND entrie.username
IF INPUT not IN entries
	RETURN error #Error inlegg finnes ikke
```
 
**Mål: Legg til et nytt inlegg til passordbehandleren.

Pseudokode:
```python
Brukeren velger legg til ny inlegg funksjonen fra hovedmenyen.
INPUT1 = INPUT

IF entrey like INPUT1 in database
	RETURN #Error inlegg med samme navn finnes allerede slett før du lager en ny.
ELSE
	INPUT2 #Tar i mot bruker navn.
	INPUT3 #Tar i mot passord.

Password.json ADD INPUT1, INPUT2, INPUT3
```

 
**Mål: Fjerne et inlegg fra passordbehandleren.

Pseudokode:
```python
#Brukeren velger fjern funksjonen fra hovedmenyen.
INPUT1 #Skriv inn navnet på inlegget du vil slette.

IF INPUT NOT in database
	RETURN #Error inlegg finnes ikke.
ELSE
	database remove entry	
``` 

**Mål: Generer tilfeldig passord.

Pseudokode:
```python
#Når du velger et passord, vil programmet spørre om du vil generere et tilfeldig passord.

IMPORT secrets # Secrets bibloteket har bygget inn funksjoner for å velge tilfeldige bokstaver tilfeldige sikre passord.

string.sybol.letter.numbers = alphabet #lager en str med alle tall bokstaver og syboler.
FOR i IN RANGE(lenght of password)
	random_password += join(secrets.choice(alphabet)) #Velger random bokstav fra streng og legger til passord.
RETURN random_password
```


