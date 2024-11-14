from data_manager import DataManager


def create_user():
    print("Welcome to JP's Flight Club.")
    print("We find the best flight deals and email you.")
    first_name = input("What is your first name?:\n").title()
    last_name = input("What is your last name?:\n").title()
    matching_emails = False

    while not matching_emails:
        first_email = input("What is your email?:\n")
        second_email = input("Type your email again.\n")
        if first_email == second_email:
            matching_emails = True
            data = DataManager()
            data.add_user(first_name, last_name, first_email)
        else:
            print("Emails don't match, try again...")


create_user()
