from cryptography.fernet import Fernet
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key()
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("Enter the master password: ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)
def view():
    with open('password.txt', 'r') as f:
        for lines in f.readlines():
            data = lines.rstrip()
            user, passw = data.split("|")
            print("User: ", user, "| Password: ", fer.decrypt(passw.encode()).decode())
def add():
    name = input("Enter the username: ")
    pwd = input("Enter the password: ")
    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Enter the mode: View password, Add password or Quit(view/add/q): ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
