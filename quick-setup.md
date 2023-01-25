THIS FILE IS FOR A QUICK STEP-BY-STEP PROCESS TO PERSONALIZING CLI(COMMAND LINE INTERFACE) PROMPT...
    - THEREFORE:
    - EXPLANATION WILL BE MINIMAL
    - INSTRUCTIONS WILL GENERALLY BE (INPUT -> OUTPUT) FORMAT
FUTURE FILES WILL BE MADE FOR BETTER FOLLOW-ALONG-INSTRUCTIONS IN ORDER TO ACHIEVE BETTER UNDERSTANDING FOR YOU AND HOPEFULLY ANYONE ELSE YOU EDUCATE ON THIS PARTICULAR TOPIC

1. GLOBAL MODIFICATION (SETTINGS WILL APPLY TO ALL USERS)
    - LOCATE global "zshrc" file
        INPUT: cd /private/etc
        OUTPUT: CHANGE DIRECTORY TO "etc" under parent "private"
        INPUT: code zshrc
        OUTPUT: OPENS PROGRAM TO CODE "zshrc"
    - MODIFY "DEFAULT PROMPT" (PS1) // EXAMPLE DEFAULT: PS1="%n@%m %1~ %# "
        - PARTS OF PS1
            - USER: %n
            - HOST: %m
            - CURRENT DIRECTORY: %1
            - HOME NAME: ~
            - END OF PROMPT: %#
        - CHANGE FORMATTING:
            - BOLD: %B{part you want bold}%b
            - UNDERLINE: %U{part you want underlined}%u
            - HIGHLIGHT: %S{part you want highlighted}%u
        - CHANGE COLOR:
            - FOREGROUND: %F{color you want}{part you want this color to apply}%f
            - BACKGROUND: %K{color you want}%k
            - USABLE COLORS
                - RED: red
                - BLUE: blue
                - GREEN: green
                - YELLOW: yellow
                - BLACK: black
                - WHITE: white
                - MAGENTA: magenta
                - CYAN: cyan
        - EXAMPLE PROMPT PERSONALIZATION
            - INPUT: PS1="%B%S%F{green}%n@Yeet%f%s%b %B%F{red}%1~ | %f%b"
            - OUTPUT:
                - USER: "manupfool" -> BOLD & GREEN
                - HOST: "Yeet" -> BOLD & GREEN
                - CURRENT DRIECTORY: "%1" -> BOLD & RED
                - HOME NAME: "~" -> BOLD & RED
                - END OF PROMPT: "| " -> BOLD & RED W/ A SPACE AFTER

2. USER MODIFICATION (SETTINGS WILL APPLY TO SPECIFIC USER)
    - LOCATE USER "zshrc" file
        INPUT: cd ~
        OUTPUT: CHANGE DIRECTORY TO "HOME"
        INPUT: ls -a
        OUTPUT: LISTS ALL FILES BOTH HIDDEN AND NOT
        - IF NO ".zshrc" FILE EXISTS
            - INPUT: touch .zshrc
            - OUTPUT: CREATE ".zshrc" FILE IN HOME
            - INPUT: code .zshrc
            - OUTPUT: OPENS PROGRAM TO CODE "zshrc" (WILL BE BLANK)
            - IN ".zshrc"
                - INPUT: PS1="%n@%m %1~ %# "
                - OUTPUT: CREATES DEFAULT PROMPT LINE
        - IF ".zshrc" FILE EXISTS
            - INPUT: code .zshrc
            - OUTPUT: OPENS PROGRAM TO CODE "zshrc"
                - IN ".zshrc"
                - INPUT: PS1="%n@%m %1~ %# "
                - OUTPUT: CREATES DEFAULT PROMPT LINE
    - MODIFY "DEFAULT PROMPT" (PS1) // EXAMPLE DEFAULT: PS1="%n@%m %1~ %# "
        - PARTS OF PS1
            - USER: %n
            - HOST: %m
            - CURRENT DIRECTORY: %1
            - HOME NAME: ~
            - END OF PROMPT: %#
        - CHANGE FORMATTING:
            - BOLD: %B{part you want bold}%b
            - UNDERLINE: %U{part you want underlined}%u
            - HIGHLIGHT: %S{part you want highlighted}%u
        - CHANGE COLOR:
            - FOREGROUND: %F{color you want}{part you want this color to apply}%f
            - BACKGROUND: %K{color you want}%k
            - USABLE COLORS
                - RED: red
                - BLUE: blue
                - GREEN: green
                - YELLOW: yellow
                - BLACK: black
                - WHITE: white
                - MAGENTA: magenta
                - CYAN: cyan
        - EXAMPLE PROMPT PERSONALIZATION
            - INPUT: PS1="%B%S%F{green}%n@Yeet%f%s%b %B%F{red}%1~ | %f%b"
            - OUTPUT:
                - USER: "manupfool" -> BOLD & GREEN
                - HOST: "Yeet" -> BOLD & GREEN
                - CURRENT DRIECTORY: "%1" -> BOLD & RED
                - HOME NAME: "~" -> BOLD & RED
                - END OF PROMPT: "| " -> BOLD & RED W/ A SPACE AFTER
