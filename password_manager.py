master_pwd = input("Please enter master password to begin: ")


def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            print(line.rstrip())

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")

def clear():
     open('password.txt', 'w').close()

while True:
    mode = input("Would you like to add a new password or view existing ones or clear the file(view, add, clear), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "clear":
        clear()
    else:
        print("Invalid mode.")
        continue