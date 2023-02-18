# =======================================================================================================
# TABLE OF CONTENTS START
# =======================================================================================================

'''
-   ORIENTATION
-   CLI REFERENCES
    -   Default Prompt Line
    -   Commands
    -   Color Options
-   FUNCTIONS
    -   Import For Functions
    -   Main Menu
    -   Colors
    -   Clear Terminal
-   END PRODUCT
'''

# =======================================================================================================
# TABLE OF CONTENTS END
# TABLE OF CONTENTS TO ORIENTATION
# ORIENTATION START
# =======================================================================================================

'''
Welcome to my script that makes personalizing your command line easy by simply running this 
script and following the input prompts!
'''

# =======================================================================================================
# ORIENTATION END
# ORIENTATION TO CLI REFERENCES
# CLI REFERENCES START
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

# =======================================================================================================
# CLI REFERENCES END
# CLI REFERENCES TO FUNCTIONS
# FUNCTIONS START
# =======================================================================================================

# ==========> IMPORT FOR FUNCTIONS <==========
import os

# ==========> MAIN MENU <==========
'''
Displays the 'Main Menu' of this script
'''
def menu():

    # vvv CHANGE DIRECTORY vvv
    home = os.path.expanduser( '~' )
    os.chdir(home)
    os.chdir('Desktop')

    # vvv MAIN MENU LIST vvv
    clear()
    while True:
        print(
            '\033[33m==========> MAIN MENU <==========\033[0m\n\n',
            '\033[36m(1) Command Line Modification\033[0m\n',
            '\033[36m(2) Alias Creation\033[0m\n',
            '\033[36m(3) Exit Program\033[0m\n'
            )
        # vvv INPUTS vvv
        start = input('What would you like to do?:\n')
        if start == '1':
            clear()
            cli_mod()
        elif start == '2':
            clear()
            print('ALIAS MOD')
        elif start == '3':
            clear()
            print('Have a great day!')
            break
        else:
            clear()
            print("Invalid Input...\n")
menu()

# ==========> MODIFICATION <==========
'''
Modify the command prompt of the command line interface.
'''
def cli_mod():
    clear()
    while True:

        # vvv IF FILE DOESN'T EXIST vvv
        if os.path.exists('test') == False:
            create_file = input("\033[33m'test'\033[0m file not found...\nWould you like to create \033[33m'test'\033[0m file? \033[33m(Y/N)\033[0m\n")
            if create_file.lower() == 'y':
                clear()
                print("Creating \033[33m'file'\033[0m...\n")
                with open('test', 'w') as f:
                    f.writelines('# =====> PROMPT <=====\n# Default Prompt:\n# PS1="%n@%m %1~ %# "\n\n# Current Prompt:\nPS1="%n@%m %1~ %# "\n\n\n# =====> ALIASES <=====')
                    f.flush()
                    f.close()
                print("\033[33m'file'\033[0m created...\n")
                break
            elif create_file.lower() == 'n':
                clear()
                print("Returning to \033[33m'Main Menu'\033[0m\n")
                break
            else:
                clear()
                print("Invalid Input...\n")

        # vvv IF FILE EXISTS vvv        
        elif os.path.exists('test') == True:
            clear()
            additional_lines = ['\nAdditional line 1\n', 'Additional line 2\n']
            with open('test', 'r') as f:
                lines = f.readlines()
            for i in range(len(lines)):
                if 'Test' in lines[i]:
                    lines[i+1:i+1] = additional_lines
            with open('test', 'w') as f:
                f.writelines(lines)
                print(lines)
                break
cli_mod()

# ==========> YE OLDE TESTING SITE <==========
import re
home = os.path.expanduser('~')
os.chdir(home)
os.chdir('Desktop')
ps1 = os.environ.get('PS1', '')
username = os.environ.get('USER', '')
hostname = os.environ.get('HOSTNAME', '')
user_re = re.compile(r'\\u')
host_re = re.compile(r'\\h')
user = user_re.search(ps1).group(0) if user_re.search(ps1) else ''
host = host_re.search(ps1).group(0) if  host_re.search(ps1) else ''

print(f"User: {username}, Host: {hostname}")
print(f"User in PS1: {user}, Host in PS1: {host}")

ps1 = os.environ.get('PS1', '')
segments = ps1.split('\\u')
if len(segments) > 1:
    segments = [segments[0]] + [s.split('\\h')[1] for s in segments[1:]]
else:
    segments = ps1.split('\\h')
username = os.environ.get('USER', '')
hostname = os.environ.get('HOSTNAME', '')
if len(segments) > 1:
    username = segments[1].split(segments[0])[-1]
    hostname = segments[1].split(segments[2])[0]
print(f"User: {username}, Host: {hostname}")

# ==========> COLORS <==========
'''
Outputs a list of all the colors available for use
'''
def colors():
    print(f"{'Color' : ^15}|{'Input' : ^15}")
    print(f"{'---------------' : ^15}|{'---------------' : ^15}")
    print(f"\033[30m{'BLACK' : ^15}\033[0m|{'black' : ^15}")
    print(f"\033[34m{'BLUE' : ^15}\033[0m|{'blue' : ^15}")
    print(f"\033[36m{'CYAN' : ^15}\033[0m|{'cyan' : ^15}")
    print(f"\033[32m{'GREEN' : ^15}\033[0m|{'green' : ^15}")
    print(f"\033[35m{'MAGENTA' : ^15}\033[0m|{'magenta' : ^15}")
    print(f"\033[31m{'RED' : ^15}\033[0m|{'red' : ^15}")
    print(f"\033[37m{'WHITE' : ^15}\033[0m|{'white' : ^15}")
    print(f"\033[33m{'YELLOW' : ^15}\033[0m|{'yellow' : ^15}")

# ==========> CLEAR TERMINAL <==========
'''
Clears the Terminal as to lessen the clutter and make reading easier
'''
def clear():
    os.system('clear')

# =======================================================================================================
# FUNCTIONS END
# FUNCTIONS TO END PRODUCT
# END PRODUCT START
# =======================================================================================================



# =======================================================================================================
# END PRODUCT END
# =======================================================================================================