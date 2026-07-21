print("=========Login system===========")
import logging
import logging_config
users = {
    "noman" : "1244",
    "ali" : "paswrod124",
    "babar": "5646"
}
def login():
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    if username in users and users[username] == password:
        print("\nLogin successful")
        logging.info(f"User '{username}' logged in.")
        print(" welcome ", username)
        logging.info(f"User '{username}' logged out.")
    else:
        print("\nInvalid username or password")
        logging.info(f"Failed login attempt for '{username}'.")
login()
         
         
    
   
