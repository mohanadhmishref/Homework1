# Muhammad Mishref CIS-3368

import mysql.connector # Used to establish the connection and submit queries to the specified mySQL server

myConnection = None # Variable for storing mySQL connection
try: # Creates mySQL connection object and attempts to connect to database.
    myConnection = mysql.connector.connect(
        host='database-1.cfmgzoc3sgka.us-east-2.rds.amazonaws.com',
        user='admin',
        password='cis3368moe',
        database='cis3368')
    print(f"Successfully connected to mySQL server.")
except mysql.connector.Error as e: # Catches mySQL error and prints to console.
    print(f"Error: {e}")

def Menu(): # Menu function which prints out all menu options.
    print(
        """
        MENU
        [a] - Add Contact
        [b] - Remove contact
        [c] - Update contact details
        [d] - Output all contacts in alphabetical order
        [e] - Output all contacts by creation date
        [f] - Output all contacts
        [q] - Quit
        """)

def execQuery(connection, query): # Function for executing mySQL query such as adding/remove contacts
    try:
        cursor = connection.cursor() # Creates cursor for query execution
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")


def execute_read_query(connection, query):  # Function which executes query and returns selected table data.
    result = None
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except mysql.connector.Error as e:
        print(f"Error: {e}")

Menu() # Call for menu function which displays choices.
userChoice = str(input("Enter your option: ")).lower() # Variable for storing user choice

while (userChoice != 'q'): # Loop for selecting menu choice until the user quits by pressing 'q'

    if userChoice == 'a':
        print("Selected Option: Add Contact")
        inputDetails = str(input("Name of Contact: "))
        inputDate = str(input("Date [MM-DD-YYYY]: "))
        add_contact = "INSERT INTO contacts (contactDetails, creationDate) VALUES ('{a}','{b}')".format(a=inputDetails, b=inputDate)
        execQuery(myConnection, add_contact)

    elif userChoice == 'b':
        print("Selected Option: Remove Contact")
        inputID = int(input("Enter ID of Contact to Remove: "))
        del_contact = "DELETE FROM contacts WHERE id = {id}".format(id=inputID)
        execQuery(myConnection, del_contact)

    elif userChoice == 'c':
        print("Selected Option: Update Contact")
        idNum = int(input("Enter ID of Contact to Update: "))
        newDetails = str(input("Enter New Name of Contact: "))
        update_contact = "UPDATE contacts SET contactDetails = '{a}' WHERE id = {id}".format(a=newDetails, id=idNum)
        execQuery(myConnection, update_contact)

    elif userChoice == 'd':
        print("Selected Option: Output Contacts by Alphabetical Order")
        output_alphabetical = "SELECT * FROM contacts ORDER BY contactDetails ASC"
        print(execute_read_query(myConnection, output_alphabetical))

    elif userChoice == 'e':
        print("Selected Option: Output Contacts by Creation Date")
        output_date = "SELECT * FROM contacts ORDER BY creationDate ASC"
        print(execute_read_query(myConnection, output_date))

    elif userChoice == 'f':
        print("Selected Option: Output Contacts")
        output_contacts = "SELECT * FROM contacts ORDER BY id ASC"
        print(execute_read_query(myConnection, output_contacts))
    else:
        print("Invalid Option.")

    Menu()
    userChoice = str(input("Enter your option: ")).lower()

print("Exiting...")