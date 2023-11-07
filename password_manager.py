# THIS IS NOT A SECURE WAY OF STORING YOUR PASSWORDS! just a practice project
from cryptography.fernet import Fernet
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key()
'''
# only need this to run one time to generate a key

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("what is the master password? ")
key = load_key() + master_pwd.bytes
fer = Fernet()

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", passw)

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")


while True:
    mode = input("would you like to add a new password or view the existing ones? Press q to quit. (view/add/q) ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid option")
        continue