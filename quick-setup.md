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
<ul>
    <li><a href="#Prompt_Modification">CLI Prompt Modification</li>
    <li><a href="#Alias_Modification">CLI Alias Modification</li>
</ul>





<!--- CLI Prompt Modification -->
<details>
<summary>CLI Prompt Modification</summary>
<p>
<a id="Prompt_Modification"></a>
<head>
    <h2 align="center">
        <b><u><i>
        CLI PROMPT MODIFICATION
        </b></u></i>
    </h2>
</head>
<br>

1. ***GLOBAL MODIFICATION (SETTINGS WILL APPLY TO ALL USERS)***
    - ***LOCATE global "zshrc" file***
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

2. ***USER/LOCAL MODIFICATION (SETTINGS WILL APPLY TO SPECIFIC USER)***
    - ***LOCATE USER/LOCAL "zshrc" file***
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
        <a href="#Prompt_Modification" target="_parent">Test</a>
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
</p>
</details>





<!--- CLI Alias Modification -->
<a id="Alias_Modification"></a>
<head>
    <h2 align="center">
        <b><u><i>
        CLI ALIAS MODIFICATION
        </b></u></i>
    </h2>
</head>