from cryptography.fernet import Fernet
import os

def generate_key():
    return Fernet.generate_key()

def load_key():
    try:
        with open("key.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        print("Key file not found.")
        return None

def get_password_key(master_password):
    key = load_key()
    if key:
        return key + master_password.encode()
    return None

def initialize_key():
    key = generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def view_passwords(fernet):
    try:
        with open("passwords.txt", "r") as f:
            for line in f:
                data = line.strip().split("|")
                if len(data) == 2:  # Check if the line has the expected format
                    user = data[0]
                    try:
                        password = fernet.decrypt(data[1].encode()).decode()
                        print("User:", user, "| Password:", password)
                    except Exception as e:
                        print("Error decrypting password for user", user, ":", str(e))
                else:
                    print("Skipping line due to incorrect format:", line.strip())
    except FileNotFoundError:
        print("Password file not found.")

def add_password(fernet):
    name = input("Account Name: ")
    password = input("Password: ")
    confirm_password = input("Confirm Password: ")
    
    if password != confirm_password:
        print("Passwords do not match.")
        return
    
    encrypted_password = fernet.encrypt(password.encode()).decode()
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + encrypted_password + "\n")
    print("Password added successfully.")

def main():
    master_password = input("What is the master password? ")
    key = get_password_key(master_password)
    if not key:
        print("Exiting...")
        return
    
    fernet = Fernet(key)

    while True:
        mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
        if mode == "q":
            break
        
        if mode == "view":
            view_passwords(fernet)
        elif mode == "add":
            add_password(fernet)
        else:
            print("Invalid mode.")

if __name__ == "__main__":
    if not os.path.exists("key.key"):
        initialize_key()
    main()
