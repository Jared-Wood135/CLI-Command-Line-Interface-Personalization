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

def yes():
    if find_hiddentest_file is True:
        print("It exists")
    else:
        print("It does not exist")
    
find_hiddentest_file()
yes()