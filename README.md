# DuolingoLearnedWords

This code writes your learned words from Duolingo to a markdown file (.md) with translations. 

### Prerequisites

Python3
Git

### Installation

On your terminal, navigate to where you would like to install the program and enter the following:
```
git clone https://github.com/ArjunV905/DuolingoLearnedWords
```

Then navigate to the downloaded folder and enter
```
python3 app.py
```

### Usage

You can choose to write your information/preferences in the config.txt file or enter them during execution.
The program will then create a .md file with the learned words and their translation in the specified directory. 

### Config

- When entering the file path, make sure to end with a \ [or / depending on your OS] (Ex: D:\Code\DuolingoLearnedWords\)
- Make sure to fill both username and password, if entering any (Otherwise the program will prompt you to enter the details)
- Make sure to fill both filePath and fileName, if entering any (Otherwise the program will prompt you to enter the details)

**NOTE**: The username and password stored in the config.txt file is **NOT ENCRYPTED**, be careful when saving information into the file.
            You can instead enter your information when the program prompts you, as it does not save the input data in any file(s)
