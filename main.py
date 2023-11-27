from fuctions import *
choice = ""
database = "Passwords.json"
while choice.lower() != "e":

    choice = str(input("Chose an option.\n\nList Password(L)\nView entry(V)\nNew entry(N)\nRemove entry(R)\nExit(E)\n"))
    

    if  choice.lower() == "l":
        print(listall(database))

    elif choice.lower() == "v":
        website = str(input("What website do you want to view. "))
        if findpassword(database, website) == False:
            print("Entry not found")
            pause()
        else:
            password, username = findpassword(database, website)
            print(f"Username:{username}\nPassword:{password}")
            pause()

    elif choice.lower() == "n":
        pass

    elif choice.lower() == "r":
        pass


    

    else:
        print("Option not found")