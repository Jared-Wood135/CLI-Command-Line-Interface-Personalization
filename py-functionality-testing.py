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
    -   Colors
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
home = os.path.expanduser( '~' )
os.chdir(home)
with open('.zshrc', 'r') as f:
    reader = f.readlines()
    test = ([row for row in reader if 'PS1' in row])
    test

# ==========> COLORS <==========
def colors():
    print(f"{'Color' : ^15}|{'Input' : ^15}")
    print(f"{'---------------' : ^15}|{'---------------' : ^15}")
    print

# =======================================================================================================
# FUNCTIONS END
# FUNCTIONS TO END PRODUCT
# END PRODUCT START
# =======================================================================================================



# =======================================================================================================
# END PRODUCT END
# =======================================================================================================