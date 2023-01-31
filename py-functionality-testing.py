import os

# Changes directory successfully
(os.chdir("/private/etc/"))
print(os.getcwd())

# Return bool if file exists
print(os.path.isfile("zshrc"))

#Opens file
#os.open("/private/etc/zshrc")

#Finds home directory
home = os.path.expanduser( '~' )
print(home)
os.chdir(home)
print(os.getcwd())

#test
#f = open("/private/etc/zshrc")
#print(f.read())

# Find then create file test
def find_hiddentest_file():
    home = os.path.expanduser( '~' )
    os.chdir(home)
    os.chdir("Desktop")
    print(os.getcwd())
    print(os.path.isfile("test"))
    if os.path.isfile("test"):
        print("You have an existing file")
        x = input("Would you like to change this file? (Yes/No)")
        if x == "Yes":
            print("Opening 'test' file now")
            os.open("home/Desktop/test")
        elif x == "No":
            print("See you later!")
        else:
            print("I'm sorry, would you like to change this file? (Yes/No)")

    else:
        print("It does not exist")

home = os.path.expanduser( '~' )
os.chdir("codeup-data-science/CLI-Command-Line-Interface-Personalization")
print(os.getcwd())
os.open("test", os.O_WRONLY)
print(os.open("test", os.O_RDONLY))