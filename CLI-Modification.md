<!---
THIS FILE IS FOR A QUICK STEP-BY-STEP PROCESS TO PERSONALIZING CLI(COMMAND LINE INTERFACE) PROMPT...
    - THEREFORE:
    - EXPLANATION WILL BE MINIMAL
    - INSTRUCTIONS WILL GENERALLY BE (INPUT -> OUTPUT) FORMAT
FUTURE FILES WILL BE MADE FOR BETTER FOLLOW-ALONG-INSTRUCTIONS IN ORDER TO ACHIEVE BETTER UNDERSTANDING FOR YOU AND HOPEFULLY ANYONE ELSE YOU EDUCATE ON THIS PARTICULAR TOPIC
--->





<!--- File Title Header -->
<head>
    <h1 align="center">
        <b><u><i>
        CLI PERSONALIZATION
        </b></u></i>
    <br><br>
</head>





<!--- CLI Table of Contents -->
<head>
    <h2 align="center">
        <b>
        <a id="tableofcontents"></a>TABLE OF CONTENTS
        </b>
    </h2>
</head>
<ul>
    <h4 align="center">
        <b>
            <li><a href="#Prompt_Modification">CLI PROMPT MODIFICATION</a href></li>
            <li><a href="#Alias_Modification">CLI ALIAS MODIFICATION</a href></li>
        </b>
    </h4>
</ul>
<details>
<p>
<summary>IMPORTANT:</summary>
    <h5 align="center">
    In order to see any changes from a file, you must either open a new window or type in source .zshrc.
</p>
</details>


<!--- CLI Prompt Modification -->
<a id="Prompt_Modification"></a>
<head>
    <h2 align="center">
        <b><u><i>
        CLI PROMPT MODIFICATION
        </b></u></i>
    </h2>
</head>
<br>
<a href="#tableofcontents">Back to Table of Contents</a href>
    <details>
    <p>
    <summary>EXPLANATION</summary>
        <h5 align="center">
        The purpose of the following instructions is to modify your terminal's prompt line.  Please determine if you would like to modify your global(/private/etc/zshrc) or user (~/.zshrc) file before following instructions.
        </h5>
    </p>    
    </details>

1. GLOBAL MODIFICATION (CHANGES WILL APPLY TO ALL USERS)
    <details>
    <p>
    <summary>EXPLANATION</summary>
        <h5 align="center">
        Your terminal's global file is located at your "/private/etc" directory as "zshrc".  Keep in mind that changes in your <b><i>GLOBAL</b></i> file will apply to <b><i>ALL USERS</b></i>.  Think of this file as a settings page for your terminal.  Everytime you open terminal, this file is read to dicatate key bindings, prompt structure, aliases if any, and much more.  In short, if you want to personalize your CLI without any online downloads, you typically will have to modify this file.
        </h5>
    </p>
    </details>

    - ***LOCATE GLOBAL "zshrc" FILE***
        - *INPUT IN **TERMINAL***:
        ```
        cd /private/etc
        ```
        - *OUTPUT IN **TERMINAL***:
        Changes directory to *"etc"* under parent directory *"private"*
        - *INPUT IN **TERMINAL***:
        ```
        code zshrc
        ```
        - *OUTPUT IN **TERMINAL***: 
        Opens program to code *"zshrc"*
    - ***MODIFY "DEFAULT PROMPT" (PS1)***

      ***EXAMPLE DEFAULT:*** 
      ```
      PS1="%n@%m %1~ %# "
      ```
      ![Image](https://user-images.githubusercontent.com/122934893/215006026-a797a6b5-a1e6-46fa-b423-bbbc7a07d715.png)
        - **PARTS OF PS1**
            ```
            USER:
            %n
            
            SEPARATE USER AND HOST:
            @

            HOST:
            %m
            
            CURRENT DIRECTORY:
            %1
            
            HOME NAME:
            ~
            
            END OF PROMPT:
            %#
            ```
        - **CHANGE FORMATTING**:
            ```
            BOLD:
            %B{part you want bold}%b
            
            UNDERLINE:
            %U{part you want underlined}%u
            
            HIGHLIGHT:
            %S{part you want highlighted}%s
            ```
        - **CHANGE COLOR**:
            ```
            FOREGROUND:
            %F{color you want}{part you want this color to apply}%f
            
            BACKGROUND:
            %K{color you want}%k
            ```
              
            | USABLE COLORS | CODE FORMAT |
            |      ---      |     ---     |
            |      RED      |     red     |
            |      BLUE     |     blue    |
            |     GREEN     |    green    |
            |     YELLOW    |    yellow   |
            |     BLACK     |    black    |
            |     WHITE     |    white    |
            |    MAGENTA    |   magenta   |
            |      CYAN     |    cyan     |

        - **EXAMPLE PROMPT PERSONALIZATION**:
            - *INPUT IN **"~/.zshrc" AND/OR "/private/etc/zshrc"***:
            ``` 
            PS1="%B%S%F{green}%n@Yeet%f%s%b %B%F{red}%1~ | %f%b"
            ```
            - *OUTPUT IN **TERMINAL***:
            ![Image](https://user-images.githubusercontent.com/122934893/215004109-e646e190-83a3-4eda-93a9-83580dd3bb2e.png)
2. ***USER MODIFICATION (SETTINGS WILL APPLY TO SPECIFIC USER)***
    <details>
    <p>
    <summary>EXPLANATION</summary>
    <h5 align="center">
    Your terminal's user file is located at your "~" directory as ".zshrc".  Keep in mind that changes in your <b><i>USER</b></i> file will apply to <b><i>THE USER</b></i>.  Think of this file as a settings page for a user's terminal.  Everytime you open the  user's terminal, this file is read to dicatate key bindings, prompt structure, aliases if any, and much more.  In short, if you want to personalize your CLI without any online downloads, you typically will have to modify this file.  By default, a user will not typically have this file so you must create this file which is outlined in the instructions below.
    </h5>
    </p>
    </details>

    - ***LOCATE USER ".zshrc" file**
        - *INPUT IN **TERMINAL***:
        ```
        cd ~
        ```
        - *OUTPUT IN **TERMINAL***:
        Changes directory to *"HOME"*
        - *INPUT IN **TERMINAL***:
        ```
        ls -a
        ```
        - *OUTPUT IN **TERMINAL***:
        Lists all files *AND HIDDEN FILES* in directory
        - ***IF NO ".zshrc" FILE EXISTS***
            - *INPUT IN **TERMINAL***:
            ```
            touch .zshrc
            ```
            - *OUTPUT*:
            creates ".zshrc" file in home directory
            - *INPUT IN **TERMINAL***:
            ```
            code .zshrc
            ```
            - *OUTPUT IN **".zshrc"***:
            Opens program to code ".zshrc" (WILL BE BLANK)
            - *INPUT IN **".zshrc"***:
            ```
            PS1="%n@%m %1~ %# "
            ```
            - *OUTPUT IN **TERMINAL***:
            Creates Default Prompt Line
            ![Image](https://user-images.githubusercontent.com/122934893/215006026-a797a6b5-a1e6-46fa-b423-bbbc7a07d715.png)

        - ***IF ".zshrc" FILE EXISTS***
            - *INPUT IN **TERMINAL***:
            ```
            code .zshrc
            ```
            - *OUTPUT*:
            Opens program to code ".zshrc"
            - *INPUT IN **.zshrc***: 
            ```
            PS1="%n@%m %1~ %# "
            ```
            - *OUTPUT IN **TERMINAL***:
            Creates Default Prompt Line
            ![Image](https://user-images.githubusercontent.com/122934893/215006026-a797a6b5-a1e6-46fa-b423-bbbc7a07d715.png)

    - ***MODIFY "DEFAULT PROMPT" (PS1)***

      ***EXAMPLE DEFAULT:*** 
      ```
      PS1="%n@%m %1~ %# " 
      ```
      ![Image](https://user-images.githubusercontent.com/122934893/215006026-a797a6b5-a1e6-46fa-b423-bbbc7a07d715.png)
        - **PARTS OF PS1**
            ```
            USER:
            %n
            
            SEPARATE USER AND HOST:
            @

            HOST:
            %m
            
            CURRENT DIRECTORY:
            %1
            
            HOME NAME:
            ~
            
            END OF PROMPT:
            %#
            ```
        - **CHANGE FORMATTING**:
            ```
            BOLD:
            %B{part you want bold}%b
            
            UNDERLINE:
            %U{part you want underlined}%u
            
            HIGHLIGHT:
            %S{part you want highlighted}%s
            ```
        - **CHANGE COLOR**:
            ```
            FOREGROUND:
            %F{color you want}{part you want this color to apply}%f
            
            BACKGROUND:
            %K{color you want}%k
            ```

            | USABLE COLORS | CODE FORMAT |
            |      ---      |     ---     |
            |      RED      |     red     |
            |      BLUE     |     blue    |
            |     GREEN     |    green    |
            |     YELLOW    |    yellow   |
            |     BLACK     |    black    |
            |     WHITE     |    white    |
            |    MAGENTA    |   magenta   |
            |      CYAN     |    cyan     |

        - **EXAMPLE PROMPT PERSONALIZATION**:
            - *INPUT IN **"~/.zshrc" AND/OR "/private/etc/zshrc"***:
            ``` 
            PS1="%B%S%F{green}%n@Yeet%f%s%b %B%F{red}%1~ | %f%b"
            ```
            - *OUTPUT IN **TERMINAL***:
            ![Image](https://user-images.githubusercontent.com/122934893/215004109-e646e190-83a3-4eda-93a9-83580dd3bb2e.png)





<!--- CLI Alias Modification -->
<a id="Alias_Modification"></a>
<head>
    <h2 align="center">
        <b><u><i>
        CLI ALIAS MODIFICATION
        </b></u></i>
    </h2>
</head>
<br>
<a href="#tableofcontents">Back to Table of Contents</a href>
<details>
<p>
<summary>EXPLANATION</summary>
    <h5 align="center">
    Aliases are essentially shortcuts that you can define and later use in your terminal.  Creating aliases are very quick and easy to create and there's no limit to how many you can have granted that they're formated properly and you remember them.
</details>
</p>

1. ***ALIAS CREATION***

    - ***OPEN "zshrc" OR ".zshrc" FILES***
        <h5>If you don't know what "zshrc" or ".zshrc" is, please follow the "CLI PROMPT MODIFICATION" instructions for the global(zshrc) or user(.zshrc) files</h5>
    - ***CREATE ALIAS***
        - *INPUT IN **zshrc** OR **.zshrc** FILE*:
        ```
        alias What-id-you-want-changed="What-you-want-the-id-to-run"
        ```
        - *OUTPUT IN **TERMINAL***:
        Runs your specific value paired with it's respective id.
    - ***EXAMPLE ALIAS***
        - *INPUT IN **zshrc** FILE*:
        <img width="125" alt="Screenshot 2023-01-28 at 16 46 35" src="https://user-images.githubusercontent.com/122934893/215294580-66ba4c09-506a-4ac9-b5b6-b364feab8333.png">

        - *OUTPUT IN **TERMINAL***:
        <img width="561" alt="Screenshot 2023-01-28 at 16 43 19" src="https://user-images.githubusercontent.com/122934893/215294505-54c48957-0c54-468e-9a09-a01df651bcf4.png">

2. ***ALIAS LIST***
    - *INPUT IN **TERMINAL***:
    <img width="176" alt="Screenshot 2023-01-28 at 16 55 40" src="https://user-images.githubusercontent.com/122934893/215294993-d5322211-eb97-4932-a13e-057f26cb4ed0.png">

    - *OUTPUT IN **TERMINAL***:
    <img width="363" alt="Screenshot 2023-01-28 at 16 56 00" src="https://user-images.githubusercontent.com/122934893/215295013-f0f33e37-3c6d-470c-8b9b-67602af02432.png">