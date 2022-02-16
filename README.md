# DuolingoLearnedWords

This code writes your learned words from Duolingo to a markdown file (.md) with translations. 

### Installation

Install dependencies [(See below)](#Dependencies) 

Download the program through GitHub:
```
git clone https://github.com/ArjunV905/DuolingoLearnedWords
```

Run the `app.py` file through python:
```
python3 app.py
```

### Usage

You can choose to write your information/preferences in the config.txt file or enter them during execution.
The program will then create a .md file with the learned words and their translation in the specified directory. 

### Config

- When entering the file path, end with a \ [or / depending on your OS] (Ex: D:\Code\DuolingoLearnedWords\)
- Fill both username and password, if entering any (Otherwise the program will prompt you to enter the details)
- Fill both filePath and fileName, if entering any (Otherwise the program will prompt you to enter the details)

**NOTE**: The username and password stored in the config.txt file is **NOT ENCRYPTED**, be careful when saving information into the file.
            You can instead enter your information when the program prompts you, as it does not save the input data

### Dependencies

`Python3 (with requests), Git, cutlet, unidic-lite`
(Cutlet and Unidic-lite are available through pip)