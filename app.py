import sys
from Lib.duolingo.duolingo import Duolingo, DuolingoException
import os


#----------------------------------[Fields]---------------------------------------------
username = ""
password = ""
filePath = ""
fileName = ""
language = ""

#----------------------------------[Methods]--------------------------------------------
#---------------------------------------------------------------------------------------

# Removes "[", "]", and "'" from the input list and returns a string combining the text
def textCleaner(input) -> str:
    phrase = str(input[0])
    rawTransl = str(input[1])
    transl = ""
    splitWords = rawTransl.split(', ')
    for e in splitWords:
        word = ""
        for c in range(len(e)):
            if e[c] != "[" and e[c] != "]" and e[c] != "'" :
                  word += e[c]
        transl += word.capitalize() + ", "
    transl = transl[:-2]                 # Removes the ending ", " for better readability 
    return phrase + " : " + transl


#---------------------------------------------------------------------------------------
# Finding length of input word
def lengthFinder(e):
    return len(e)


#---------------------------------------------------------------------------------------
# Read login details from config.txt and return true if a value was obtained
def readLogin() -> bool:
    foundUsername = False
    foundPassword = False
    file = open(os.path.join(sys.path[0], "config.txt"), 'r')
    fileList = file.readlines()

    # Reading username
    usernameLine = fileList[0]
    readUsername = ""
    inQuotes = False
    #       Searching through the line to find the username
    for c in range(len(usernameLine)):
        if (not inQuotes and usernameLine[c] == "\""):
            inQuotes = True
        elif (inQuotes and usernameLine[c] != "\""):
            readUsername += usernameLine[c]
        elif (inQuotes and usernameLine[c] == "\""):
            inQuotes = False    
    global username 
    username = readUsername
    if (len(readUsername) > 0):
        foundUsername = True

    # Reading password
    passwordLine = fileList[1]
    readPassword = ""
    inQuotes = False
    #       Searching through the line to find the password
    for c in range(len(passwordLine)):
        if (not inQuotes and passwordLine[c] == "\""):
            inQuotes = True
        elif (inQuotes and passwordLine[c] != "\""):
            readPassword += passwordLine[c]
        elif (inQuotes and passwordLine[c] == "\""):
            inQuotes = False  
    global password
    password = readPassword
    if (len(readPassword) > 0):
        foundPassword = True
    
    file.close()
    return foundUsername and foundPassword


#---------------------------------------------------------------------------------------
# Read desired directory from config.txt and return true if a value was obtained
def readDir() -> bool:
    foundPath = False
    foundName = False
    file = open(os.path.join(sys.path[0], "config.txt"), 'r')
    fileList = file.readlines()

    # Reading file path
    pathLine = fileList[2]
    readPath = ""
    inQuotes = False
    #       Searching through the line to find the username
    for c in range(len(pathLine)):
        if (not inQuotes and pathLine[c] == "\""):
            inQuotes = True
        elif (inQuotes and pathLine[c] != "\""):
            readPath += pathLine[c]
        elif (inQuotes and pathLine[c] == "\""):
            inQuotes = False    
    global filePath 
    filePath = readPath
    if (len(readPath) > 0):
        foundPath = True

    # Reading file name
    nameLine = fileList[3]
    readName = ""
    inQuotes = False
    #       Searching through the line to find the password
    for c in range(len(nameLine)):
        if (not inQuotes and nameLine[c] == "\""):
            inQuotes = True
        elif (inQuotes and nameLine[c] != "\""):
            readName += nameLine[c]
        elif (inQuotes and nameLine[c] == "\""):
            inQuotes = False  
    global fileName
    fileName = readName
    if (len(readName) > 0):
        foundName = True
    
    file.close()
    return foundPath and foundName 

#---------------------------------------------------------------------------------------
# Read desired language from config.txt and return true if a value was obtained
def readLang() -> bool:
    foundLang = False
    file = open(os.path.join(sys.path[0], "config.txt"), 'r')
    fileList = file.readlines()

    # Reading username
    langLine = fileList[4]
    readLang = ""
    inQuotes = False
    #       Searching through the line to find the username
    for c in range(len(langLine)):
        if (not inQuotes and langLine[c] == "\""):
            inQuotes = True
        elif (inQuotes and langLine[c] != "\""):
            readLang += langLine[c]
        elif (inQuotes and langLine[c] == "\""):
            inQuotes = False    
    global language 
    language = readLang
    if (len(readLang) > 0):
        foundLang = True
    
    file.close()
    return foundLang


#------------------------------------[Main]---------------------------------------------
#---------------------------------------------------------------------------------------

# Read the config file for login, directory and language
#   Handling input of login
if (not readLogin()):
    valid = False
    inputUsername = ""
    inputPassword = ""
    while (not valid):
        print("Enter your Duolingo username:")
        inputUsername = input()
        print("Enter your password:")
        inputPassword = input()
        try:
            testLingo = Duolingo(inputUsername, inputPassword)
            print("Login successfull\n")
            valid = True
        except DuolingoException:#.DuolingoException:
            print("Incorrect username and password, try again\n")
            valid = False
    username = inputUsername
    password = inputPassword
else:
    print("Successfully read login credentials from config.txt...")

#   Handling input of directory
if (not readDir()):
    valid = False
    inputPath = ""
    inputName = "" 
    while (not valid):
        print("Enter the directory you want the file to be created in:   (Ex: D:\\Code\\DuolingoLearnedWords\\")
        inputPath = input()
        print("Enter a name for the file to store the learned words:")
        inputName = input()
        inputDir = inputPath + inputName + ".md"
        try:
            fileTest = open(inputPath + inputName + ".md", "w")
            valid = True
            print("Successfully created the file\n")
        except OSError:
            print("Invalid file path and/or name, try again\n")
    filePath = inputPath
    fileName = inputName
else:
    print("Successfully read target directory from config.txt...")

#   Handling input of language
if (not readLang()):
    valid = False
    inputLang = ""
    while (not valid):
        print("Enter the Duolingo language to store from:")
        inputLang = input()
        lingoTest = Duolingo(username, password)
        try:
            testLang = lingoTest.get_abbreviation_of(inputLang)
            testList = lingoTest.get_known_words(testLang)
            print("Valid language name\n")
            valid = True
        except:
            print("Invalid language name, try again")
            print("(Ensure that the language exists on Duolingo and a language that you have learnt or are learning)\n")
    language = inputLang
else:
    print("Successfully read target language from config.txt...\n")


# Getting the dict of learned words from duolingo
lingo = Duolingo(username, password)
sourceLang = lingo.get_abbreviation_of(language)
knownWords = lingo.get_known_words(sourceLang)

knownTransl = []
rawList = []
knownTransl = lingo.get_translations(knownWords, source=sourceLang, target='en')


# Sorting the dict into list
for sortedKey in sorted(knownTransl, key=lengthFinder):
    rawList.append([sortedKey, knownTransl[sortedKey]])


# Write to file (loop for each element in finalList)
fileDir = filePath + fileName + ".md"
file = open(fileDir, "w", encoding="utf-8")

print("Writing to " + fileDir + "...")
file.write("## Learned Phrases \n \n")
for ele in rawList:
    line = textCleaner(ele)
    file.write("%s \n" % line)       # %s indicates that the value to be added is a string    
print("Successfully written to " + fileDir)
file.close()
