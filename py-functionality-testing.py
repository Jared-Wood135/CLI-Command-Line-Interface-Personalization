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
    -   Prompt Line Modification
    -   Alias Modification
    -   Misc List
    -   Colors List
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
'''
All imports needed for this script to work properly
'''
import os

# ==========> MAIN MENU <==========
'''
Displays the 'Main Menu' of this script
'''
def menu():

    # vvv CHANGE DIRECTORY vvv
    home = os.path.expanduser( '~' )
    os.chdir(home)

    # vvv MAIN MENU LIST vvv
    clear()
    error = "\033[31mInvalid Input...\033[0m\n"
    while True:
        # vvv IF FILE DOESN'T EXIST vvv
        if os.path.exists('.zshrc') == False:
            create_file = input("\033[33m'.zshrc'\033[0m file not found...\nWould you like to create \033[33m'.zshrc'\033[0m file? \033[33m(Y/N)\033[0m\n")
            if create_file.lower() == 'y':
                clear()
                print("Creating \033[33m'.zshrc'\033[0m file...\n")
                with open('.zshrc', 'w') as f:
                    f.writelines('# =====> PROMPT <=====\n# Default Prompt:\n# PS1="%n@%m %1~ %# "\n\n# Current Prompt:\nPS1="%n@%m %1~ %# "\n\n\n# =====> ALIASES <=====')
                    f.flush()
                    f.close()
                print("\033[33m'.zshrc'\033[0m file created...\n")
            elif create_file.lower() == 'n':
                clear()
                print("Have a great day!")
                break
            else:
                clear()
                print(error)
        # vvv IF FILE EXISTS vvv        
        elif os.path.exists('.zshrc') == True:
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
                alias_mod()
            elif start == '3':
                clear()
                print('Have a great day!')
                break
            else:
                clear()
                print(error)

# ==========> PROMPT LINE MODIFICATION FUNCTION <==========
'''
Modify the command prompt of the command line interface.
'''
def cli_mod():
    clear()
    colors_list = ['black', 'blue', 'cyan', 'green', 'magenta', 'red', 'white', 'yellow', 'none']
    misc_list = ['bold', 'highlight', 'both', 'none']
    error = "\033[31mInvalid Input...\033[0m\n"
    while True:

        # vvv IF FILE DOESN'T EXIST vvv
        if os.path.exists('.zshrc') == False:
            create_file = input("\033[33m'.zshrc'\033[0m file not found...\nWould you like to create \033[33m'.zshrc'\033[0m file? \033[33m(Y/N)\033[0m\n")
            if create_file.lower() == 'y':
                clear()
                print("Creating \033[33m'file'\033[0m...\n")
                with open('.zshrc', 'w') as f:
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
                print(error)

        # vvv IF FILE EXISTS vvv        
        elif os.path.exists('.zshrc') == True:

            # vvv STARTING PROMPT INPUT vvv
            clear()
            print('"\033[33mHOST@USER\033[0m %1~ %# "\n')
            host_user = input("What would you like your \033[33mstarting prompt\033[0m to be?\n")
            
            # vvv STARTING PROMPT COLOR vvv
            clear()
            while True:
                colors()
                print('\n"\033[33mHOST@USER\033[0m %1~ %# "\n')
                host_user_color = input("What \033[33mcolor\033[0m do you want for your \033[33mstarting prompt\033[0m?\n")
                if host_user_color.lower() in colors_list:
                    if host_user_color.lower() == 'none':
                        host_user_result = (host_user)
                        break
                    else:
                        host_user_result = ("%F{" + host_user_color + "}" + host_user + "%f")
                        break
                else:
                    clear()
                    print(error)

            # vvv STARTING PROMPT MISC vvv
            clear()
            while True:
                misc()
                print('\n"\033[33mHOST@USER\033[0m %1~ %# "\n')
                host_user_misc = input("What \033[33mmodifier\033[0m would you like to apply to your \033[33mstarting prompt\033[0m?\n")
                if host_user_misc.lower() in misc_list:
                    if host_user_misc.lower() == 'bold':
                        host_user_mod_begin = '%B'
                        host_user_mod_end = '%b'
                        break
                    elif host_user_misc.lower() == 'highlight':
                        host_user_mod_begin = '%S'
                        host_user_mod_end = '%s'
                        break
                    elif host_user_misc.lower() == 'both':
                        host_user_mod_begin = '%B%S'
                        host_user_mod_end = '%s%b'
                        break
                    elif host_user_misc.lower() == 'none':
                        host_user_mod_begin = ''
                        host_user_mod_end = ''
                        break
                    break
                else:
                    clear()
                    print(error)

            # vvv WORKING DIRECTORY COLOR vvv
            clear()
            while True:
                colors()
                print('\n"HOST@USER \033[33m%1~\033[0m %# "\n')
                cwd_color = input("What \033[33mcolor\033[0m do you want for your \033[33mcurrent working directory\033[0m?\n")
                if cwd_color.lower() in colors_list:
                    if cwd_color.lower() == 'none':
                        cwd_result = '%1~'
                        break
                    else:
                        cwd_result = ("%F{" + cwd_color + "}%1~" + "%f")
                        break
                else:
                    clear()
                    print(error)

            # vvv WORKING DIRECTORY MISC vvv
            clear()
            while True:
                misc()
                print('\n"HOST@USER \033[33m%1~\033[0m %# "\n')
                cwd_misc = input("What \033[33mmodifier\033[0m would you like to apply to your \033[33mcurrent working directory\033[0m?\n")
                if cwd_misc.lower() in misc_list:
                    if cwd_misc.lower() == 'bold':
                        cwd_mod_begin = '%B'
                        cwd_mod_end = '%b'
                        break
                    elif cwd_misc.lower() == 'highlight':
                        cwd_mod_begin = '%S'
                        cwd_mod_end = '%s'
                        break
                    elif cwd_misc.lower() == 'both':
                        cwd_mod_begin = '%B%S'
                        cwd_mod_end = '%s%b'
                        break
                    elif cwd_misc.lower() == 'none':
                        cwd_mod_begin = ''
                        cwd_mod_end = ''
                        break
                    break
                else:
                    clear()
                    print(error)

            # vvv ENDING PROMPT INPUT vvv
            clear()
            print('"HOST@USER %1~ \033[33m%#\033[0m "\n')
            end_prompt = input("What would you like your \033[33mending prompt\033[0m to be?\n")
            
            # vvv ENDING PROMPT COLOR vvv
            clear()
            while True:
                colors()
                print('\n"HOST@USER %1~ \033[33m%#\033[0m "\n')
                end_prompt_color = input("What \033[33mcolor\033[0m do you want for your \033[33mending prompt\033[0m?\n")
                if end_prompt_color.lower() in colors_list:
                    if end_prompt_color.lower() == 'none':
                        end_prompt_result = (end_prompt)
                        break
                    else:
                        end_prompt_result = ("%F{" + end_prompt_color + "}" + end_prompt + "%f")
                        break
                else:
                    clear()
                    print(error)

            # vvv ENDING PROMPT MISC vvv
            clear()
            while True:
                misc()
                print('\n"HOST@USER %1~ \033[33m%#\033[0m "\n')
                end_prompt_misc = input("What \033[33mmodifier\033[0m do you want for your \033[33mending prompt\033[0m?\n")
                if end_prompt_misc.lower() in misc_list:
                    if end_prompt_misc.lower() == 'bold':
                        end_prompt_mod_begin = '%B'
                        end_prompt_mod_end = '%b'
                        break
                    elif end_prompt_misc.lower() == 'highlight':
                        end_prompt_mod_begin = '%S'
                        end_prompt_mod_end = '%s'
                        break
                    elif end_prompt_misc.lower() == 'both':
                        end_prompt_mod_begin = '%B%S'
                        end_prompt_mod_end = '%s%b'
                        break
                    elif end_prompt_misc.lower() == 'none':
                        end_prompt_mod_begin = ''
                        end_prompt_mod_end = ''
                        break
                    break
                else:
                    clear()
                    print(error)

            # vvv CREATING NEW PS1 vvv
            clear()
            with open('.zshrc', 'r') as f:
                lines = f.readlines()
            for i in range(len(lines)):
                if lines[i].startswith('PS1'):
                    lines[i] = lines[i].replace(lines[i], (f"PS1=\"{host_user_mod_begin}{host_user_result}{host_user_mod_end} {cwd_mod_begin}{cwd_result}{cwd_mod_end} {end_prompt_mod_begin}{end_prompt_result}{end_prompt_mod_end} \"\n"))
            with open('.zshrc', 'w') as f:
                f.writelines(lines)
                print("\033[32mCommand Line Prompt Line Changed Successfully\033[0m\n")
                break

# ==========> ALIAS MODIFICATION FUNCTION <==========
'''
Add aliases to file
'''
def alias_mod():
    clear()
    alias_name = input("What \033[33mname\033[0m do you want to call your \033[33malias\033[0m?\n")
    clear()
    alias_output = input("What do you want \033[33m" + alias_name + "\033[0m to do?\n")
    clear()
    with open('.zshrc', 'r') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if lines[i].startswith('# =====> ALIASES <====='):
                lines[i] = lines[i].replace(lines[i], (lines[i] + '\nalias ' + alias_name + '=\'' + alias_output + '\''))
    with open('.zshrc', 'w') as f:
        f.writelines(lines)
        print(f"\033[32mSuccessfully created alias\033[0m \033[33m{alias_name}\033[0m \033[32mcreated to output\033[0m \033[33m{alias_output}\033[0m\n")

# ==========> MISC LIST FUNCTION <==========
'''
Outputs a list of additional modifications for the command prompt
'''
def misc():
    print(f"{'Modifier' : ^20}|{'Input' : ^20}")
    print(f"{'--------------------' : ^20}|{'--------------------' : ^20}")
    print(f"{'BOLD TEXT' : ^20}|{'bold' : ^20}")
    print(f"{'HIGHLIGHTED TEXT' : ^20}|{'highlight' : ^20}")
    print(f"{'BOLD & HGHLGT' : ^20}|{'both' : ^20}")
    print(f"{'NONE' : ^20}|{'none' : ^20}")

# ==========> COLORS LIST FUNCTION <==========
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
    print(f"{'NONE' : ^15}|{'none' : ^15}")

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

menu()

# =======================================================================================================
# END PRODUCT END
# =======================================================================================================