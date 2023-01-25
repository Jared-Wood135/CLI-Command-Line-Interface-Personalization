# CLI-Command-Line-Interface-Personalization
Instruction and education of personalizing CLI for better efficiency and effectiveness.  (WORK IN-PROGRESS)

NOTES ON PROCEDURE FOLLOWS - WILL BE REORGANIZED LATER BUT FOR NOW ACTS AS SCRATCH
* TERMINAL:
    - $PS1 = $PROMPT
        - OUTPUTS YOUR TERMINAL PROMPT
            - DEFAULT OUTPUT: %n@%m %1~ %#
                - "%n" = USER NAME
                - "%m" = HOST NAME
                - "%1" = CURRENT DIRECTORY
                - "~" = IF CURRENT DIRECTORY IS HOME THEN DISPLAY "~"
                - "%#" = SYMBOL IMMEADIATELY BEFORE INPUT
    - Terminal -> Settings -> Profiles
        - Left hand side are themes to quickly change terminal format
    - GLOBAL ZSHELL FOLDER
        - CHANGES HERE APPLY TO ALL USERS ON THE SYSTEM
        - INPUT: cd /private/etc
            - OUTPUT: ROUTES TO FOLDER
        - INPUT: ls zs*
            - OUTPUT: LISTS ALL ELEMENTS THAT START WITH "zs"
        - FIND ELEMENT "zshrc"
        - INPUT: code zshrc
            - LAUNCH PROGRAM IOT CODE "zshrc"
        - INPUT:
    - USER ZSHELL FOLDER
        - CHANGES HERE APPLY TO SPECIFIC USER ON THE SYSTEM
        - DEFAULT USER WILL NOT HAVE A "zshrc" THUS MUST CREATE ONE FIRST
        - INPUT: cd ~
            - OUTPUT: ROUTES TO HOME DIRECTORY
        - INPUT: touch .zshrc
            - OUTPUT: CREATE HIDDEN FOLDER NAMED "zshrc"
        - INPUT: code .zshrc
            - OUTPUT: LAUNCH PROGRAM IOT CODE ".zshrc"
    - FIND PROMPT LINE IN PROGRAM
        - IF IN GLOBAL, PS1="%n@%m %1~ %#", WILL ALREADY EXIST
        - IF IN USER, PS1="%n@%m %1~ %#", WILL NEED TO BE CREATED ON A NEW LINE IOT MODIFY
        - COLOR:
            - CHANGE FOREGROUND COLOR
                - %F{color}<SECTION YOU WANT TO BE A SPECIFIC COLOR>%f
                    COLORS: black, red, green, yellow, blue, magenta, cyan, white
            - CHANGE BACKGROUND COLOR
                - %K{color}%k
        - FONTS:
            - BOLD
                - %B<INPUT>%b
            - UNDERLINE
                - %U<INPUT>%u
            - HIGHLIGHT
                - %S<INPUT>%s

