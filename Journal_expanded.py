# Journal program originally adapted from
# https://github.com/CandaceJWilliams/python-journal


import datetime
import os

author = "Julian"


# -----------------------------------Define Functions-------------------------------------------- #

def create_journal():
    name = input("Name your journal: ")  

    cwd = os.getcwd()  
    path = cwd + "/" + name  

    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path + "\n")
    else:
        print("Successfully created the directory!" + "\n")

    entry_controls()


def open_journal():
    os.chdir(os.getcwd())  
    journal_list = os.listdir()  
    if len(journal_list) == 0:
        os.chdir('..')
    else:

        print("\n" + "Current # of Journals: " + str(len(journal_list)))
        print("---------Journals---------")
        for journal in journal_list:
            print(journal)  

        name = input("\n" + "Name of journal: ")  
        cwd = os.getcwd()  
        path = cwd + "/" + name  
        os.chdir(path)  

        directory_list = os.listdir()  
        print("\n" + "Current Entries: " + str(len(directory_list)))
        for entry in directory_list:
            print(entry)  

        entry_controls()


def fetch_content():
    new_content = input("Tell me all of your secrets: ")  
    return new_content


def add_content():
    directory_list = os.listdir()  

    # print("Available entries: ")
    # for entry in directory_list:
    #    print(entry)

    title = input("What's the title of your entry? ")  

    filename = title.replace(" ", "") + ".txt"  
    if filename in directory_list:
        print("Well done. Opening entry.")
    elif filename not in directory_list:
        print("Invalid user entry or no entries currently exist in this journal." + "\n" + "Please try again: ")
        add_content()
    else:
        return

    entry = open(filename, "a+")  
    for line in entry:
        print(line) # Can't seem to get add_content() to print the existing text

    entry.write("\n\n")
    entry.write(author + "\n")  
    entry.write(title + "\n")  
    entry.write(str(datetime.datetime.now()) + "\n")  

    content = fetch_content()  # Grab content

    count = 0
    entry.write("\n")
    for i in range(0, len(content)):
        entry.write(content[i])
        if content[i] == " ":  
            count += 1
            # print(count) Use this for debugging the count if it isn't incrementing properly
            if count >= 10:
                entry.write("\n")
                count = 0

    entry.close()
    choice()


def add_page():
    title = input("Name your entry: ")
    filename = title.replace(" ", "") + ".txt"
    entry = open(filename, "a+")
    entry.close()
    entry_controls()


def remove_page():
    title = input("What's the title of your entry? ")
    filename = title.replace(" ", "") + ".txt"
    os.remove(filename)
    choice()


def journal_controls():
    print("\n\n")
    print("What would you like to do?: ")
    print("1: Create a journal")
    print("2: Open a journal")
    print("3: Exit program")
    option = input("\n" + "Your choice: ")
    

    if option == "1" or option == 1:
        create_journal()
    elif option == "2" or option == 2:
        open_journal()
    elif option == "3" or option == 3:
        print("\n" + "Have a great day!" "\n")
    else:
        print("Please answer based on the available choices")
        journal_controls()
    


def entry_controls():
    directory_list = os.listdir()  

    if len(directory_list) == 0:
        option = input("No entries currently exist. Would you like to create an entry? (y/n): ")
        if option == "y" or option == "yes":
            add_page()
        elif option == "n" or option == "no":
            print("Returning to main menu...")
            journal_controls()
    else:
        print("\n" + "Available entries: ")
        for entry in directory_list:
            print(entry)
        print("\n" + "What would you like to do?: ")
        print("1: Create an entry")
        print("2: Add to an entry")
        print("3: Remove an entry")
        print("4: Return to Main Menu")
        option = input("\n" + "Your choice: ")
    
        if option == "1" or option == 1:
            add_page()
        elif option == "2" or option == 2:
            add_content()
        elif option == "3" or option == 3:
            remove_page()
        elif option == "4" or option == 4:
            journal_controls()
        else:
            print("Please answer based on the available choices")
            entry_controls()

def choice():
    choice = input("Do you need to do anything else? (y/n)")
    if choice == "y" or choice == "yes":
        controls()
    elif choice == "n" or choice == "no":
        print("Have a great day!")
    elif choice != "y" or choice != "yes" or choice != "n" or choice != "no":
        choice = input("Invalid entry. Please select (y/n): ")




# -----------------------------------Program Begin-------------------------------------------- #

check_author = input("Please enter your name: ")
if check_author != author:
    print("\n" + "Unauthorized user. How did you get here?")
    print("Nevermind, program will terminate now. Have a great day!" + "\n")
elif check_author == author:
    print("\n" + "Welcome, " + author + "!")
    journal_controls()
