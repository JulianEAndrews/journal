import datetime
import os

author = ""


# -----------------------------------Define Functions--------------------------------------------#

def create_journal():
    name = input("Name your journal: ")  # Ask for a name for the journal

    cwd = os.getcwd()  # Uses os import to get current path
    path = cwd + "/" + name  # Concatenate to create a new path

    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory!")


def open_journal():
    os.chdir(os.getcwd())  # change the directory to the current path
    journal_list = os.listdir()  # get list of the journals within the current directory

    print("Current # of Journals: " + str(len(journal_list)))
    for journal in journal_list:
        print(journal)  # Print out each journal name

    name = input("Name of journal: ")  # Ask user to select a journal
    cwd = os.getcwd()  # Find directory we're in
    path = cwd + "/" + name  # update path
    os.chdir(path)  # Change directories to the path we determined

    directory_list = os.listdir()  # Get a list of entries
    print("Current Entries: " + str(len(directory_list)))
    for entry in directory_list:
        print(entry)  # Display entries for the user


def fetch_content():
    content_list = os.listdir()
    if exiting_content in content_list:
        print(existing_content)
    new_content = input("Write till your heart's content: ")  # Input
    return new_content


def add_content():
    directory_list = os.listdir()  # List the entries
    print("Available entries: ")
    for entry in directory_list:
        print(entry)
    title = input("What's the title of your entry? ")  # Get a title
    filename = title.replace(" ", "") + ".txt"  # Updates journal entry
    if filename in directory_list:
        print("Heck yeah, dude. Well done.")
    else:
        print("Ya done messed up, exiting now.")
        return
    content = fetch_content()  # Grab content
    entry = open(filename, "a")  # Create/open our file
    entry.write("\n\n")
    entry.write(author + "\n")  # Add the user's name
    entry.write(title + "\n")  # Add the chosen title
    entry.write(str(datetime.datetime.now()) + "\n")  # Add the date

    count = 0
    entry.write("\n")
    for i in range(0, len(content)):
        entry.write(content[i])
        if content[i] == " ":  # determine if we have a space and increase the counter
            count += 1
            # print(count) Use this for debugging the count if it isn't incrementing properly
            if count >= 10:
                entry.write("\n")
                count = 0

    entry.close()


def add_page():
    title = input("Name your entry: ")
    filename = title.replace(" ", "") + ".txt"
    add_content()


def remove_page():
    title = input("What's the title of your entry? ")
    filename = title.replace(" ", "") + ".txt"
    os.remove(filename)


def controls():
    print("What would you like to do?: ")
    print("1: Create a journal")
    print("2: Open a journal")
    print("3: Create an entry")
    print("4: Add to an entry")
    print("5: Remove an entry")
    option = input("Your choice: ")
    print("-----\n-----")
    # ^^This prefaces the userwith options and asks for input

    if option == "1" or option == 1:
        create_journal()
    elif option == "2" or option == 2:
        open_journal()
    elif option == "3" or option == 3:
        add_page()
    elif option == "4" or option == 4:
        add_content()
    elif option == "5" or option == 5:
        remove_page()
    else:
        print("Please answer based on the available choices")
        controls()
    # Conditions that execute functions based on user's choice

    choice = input("Do you need to do anything else? (y/n)")
    if choice == "y" or choice == "yes":
        controls()
    elif choice == "n" or choice == "no":
        print("Have a great day!")
    elif choice != "y" or choice != "yes" or choice != "n" or choice != "no":
        choice = input("Invalid entry. Please select (y/n): ")

    # Asks if the user wants to do anything else. If not,
    # The program ends


author = input("What's your name? ")
controls()
