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
f = os.open("test", os.O_WRONLY)


home = os.path.expanduser( '~' )
os.chdir(home)
with open('.zshrc', 'r') as f:
    reader = f.readlines()
    test = ([row for row in reader if 'PS1' in row])
    test
# =======================================================================================================
# CLI REFERENCES
# =======================================================================================================

# ==========> DEFAULT PROMPT LINE <==========
'''
PS1="%n@%m %1~ %# "

%n - HOST
%m - USER
%1 - CURRENT DIRECTORY
~ - HOME
%# - PROMPT ENDER
'''

# ==========> COMMANDS <==========
'''
%B{Input}%b ==> Boldens Input
%S{Input}%s ==> Highlights Input
%F{COLOR}{Input}%f ==> Changes Color of Input
%K{COLOR}{Input}%k ==> Changes Color of Background
'''

# ==========> COLOR OPTIONS <==========
'''
green
red
black
white
cyan
magenta
yellow
gray
'''