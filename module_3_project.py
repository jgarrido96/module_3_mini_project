
contacts = {}
def home_page():
    while True:
        user_input = input(str("\nWelcome to the Jungle Management System!\nMenu:\n1. Add a new contact\n2. Edit an existing contact\n3. Delete a contact\n4. Search for a contact\n5. Display all contacts\n6. Export contacts to a text file\n7. Quit\n"))
        try:
            if user_input.isnumeric():
                if int(user_input) > 7 or int(user_input) <1:
                    print("Invalid entry, please select something from the menu.")
                    continue
                else:
                    if user_input == "1":
                        add_contact()
                    elif user_input == "2":
                        edit_contact()
                    elif user_input == "3":
                        delete_contacts()
                    elif user_input == "4":
                        search_contacts()
                    elif user_input == "5":
                        print_contacts()
                    elif user_input == "6":
                        export_contacts()
                    elif user_input == "7":
                        print("Now leaving the Jungle Management System...\nThank you!")
                        break
            else:
                print("Invalid entry, please select something from the menu.")
        except Exception as e:
            print(f"An error occured: {e}")


def add_contact():
    email = input("Enter an Email: ")
    phone_number = input("Enter a Phone Number: ")
    first_name = input("Enter a First Name: ")
    last_name = input("Enter a Last Name: ")
    notes = input("Add notes if you'd like: ")

    contacts[email] = {"Email": email, "Phone number": phone_number, "First name": first_name, "Last name": last_name, "Notes": notes}
    print_contacts()
    



def print_contacts():
    print(f"Your contacts:\n")
    for contact in contacts:
        print(f"Last name: {contacts[contact]["Last name"]}\nFirst name: {contacts[contact]["First name"]}\nEmail: {contacts[contact]["Email"]}\nPhone number: {contacts[contact]["Phone number"]}\nNotes: {contacts[contact]["Notes"]}\n\n")



def edit_contact():
    print_contacts()
    user_input = input("Please enter the email you'd like to edit: ")
    if user_input not in contacts:
        print("Contact not found, please enter a valid email.")
    else:
        email = input("Enter a new Email or hit 'ENTER' for no change: ")
        phone_number = input("Enter a new Phone Number or hit 'ENTER' for no change: ")
        first_name = input("Enter a new First Name or hit 'ENTER' for no change: ")
        last_name = input("Enter a new Last Name or hit 'ENTER' for no change: ")
        notes = input("Add notes if you'd like or hit 'ENTER' for no change: ")
        for contact in contacts:
            if contact == user_input:
                if email != "":
                    contacts[user_input]["Email"] = email
                if phone_number != "":
                    contacts[user_input]["Phone number"] = phone_number
                if first_name != "":
                    contacts[user_input]["First name"] = first_name
                if last_name != "":
                    contacts[user_input]["Last name"] = last_name
                if notes != "":
                    contacts[user_input]["Notes"] = notes
        print_contacts()

def search_contacts():
    print_contacts()
    user_input = input("Please enter the email you'd like to view: ")
    if user_input not in contacts:
        print("Contact not found, please enter a valid email.")
    else:
        for contact in contacts:
            if contact == user_input:
                print(f"Last name: {contacts[contact]["Last name"]}\nFirst name: {contacts[contact]["First name"]}\nEmail: {contacts[contact]["Email"]}\nPhone number: {contacts[contact]["Phone number"]}\nNotes: {contacts[contact]["Notes"]}\n\n")

def delete_contacts():
    print_contacts()
    user_input = input("Please enter the email you'd like to delete: ")
    if user_input not in contacts:
        print("Contact not found, please enter a valid email.")
    else:
        del contacts[user_input]
        print(f"{user_input} deleted successfully")

def export_contacts():
    print_contacts()
    with open(r"C:\Users\jgarr\Documents\coding_temple\backend\Week_3\module_3_project\contacts.txt", "w") as file:
        for contact in contacts:
            file.write(f"Last name: {contacts[contact]["Last name"]}\nFirst name: {contacts[contact]["First name"]}\nEmail: {contacts[contact]["Email"]}\nPhone number: {contacts[contact]["Phone number"]}\nNotes: {contacts[contact]["Notes"]}\n\n")
    print("Your file has been created!")


home_page()     
            
            