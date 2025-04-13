#Code by


from colorama import init as colorinit
from colorama import Style
from colorama import Fore
import random

genresFile = ".genres.txt"
themesFile = ".themes.txt"
featuresFile = ".features.txt"
nounsFile = ".nouns.txt"
adjectivesFile = ".adjectives.txt"


colorinit()
random.seed()

def GetMode():
    print(f"{Fore.WHITE}{Style.BRIGHT}" + "Select Mode:"+ f"{Style.RESET_ALL}")
    print("[1] Simple Mode\n[2] Detailed Mode\n[3] Add element to list")
    usrInput = int(input())
    if usrInput >= 1 and usrInput <= 3:
        return usrInput
    else:
        print("Invalid selection.")
        return GetMode()

def RunSimple():
    rules = """1. You will get 3 random Steam tags, if needed, you must include at least two of them.
2. You will get 2 random words to kickstart brainstorming, you are free to use them or discard them.\n"""

    file = open(genresFile,"r")
    tags = file.readlines()
    file.close()

    file = open(themesFile,"r")
    tags.extend(file.readlines())
    file.close()

    file = open(featuresFile,"r")
    tags.extend(file.readlines())
    file.close()

    file = open(nounsFile,"r")
    nouns = file.readlines()
    file.close()

    file = open (adjectivesFile,"r")
    adjectives = file.readlines()
    file.close()

    randomTag01 = random.randrange(0,len(tags))
    randomTag02 = random.randrange(0,len(tags))
    randomTag03 = random.randrange(0,len(tags))
    randomNoun = random.randrange(0,len(nouns))
    randomAdjective = random.randrange(0,len(adjectives))

    print(f"{Fore.GREEN}{Style.BRIGHT}" + "RUNNING IN SIMPLE MODE: \n" + f"{Style.RESET_ALL}")

    print(f"{Fore.WHITE}{Style.BRIGHT}" + rules + f"{Style.RESET_ALL}")
    print(f"{Fore.BLUE}{Style.BRIGHT}" + "Your random Steam tags are: " + f"{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{Style.BRIGHT}" + tags[randomTag01] + tags[randomTag02] + tags[randomTag03] + f"{Style.RESET_ALL}")

    print(f"{Fore.RED}{Style.BRIGHT}" + "Your random word set is: " + f"{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{Style.BRIGHT}" + (adjectives[randomAdjective] + nouns[randomNoun]).title() + f"{Style.RESET_ALL}")

def RunDetailed():
    rules = """1. You will get two random genres for the game, you may use one or both.
2. You will get two random themes, you may use one or both.
3. You will get two random features, you may use one or both
4. You will get two random words to kickstart brainstorming, you are free to use or discard them.\n"""
    file = open(genresFile,"r")
    genres = file.readlines()
    file.close()

    file = open(themesFile,"r")
    themes =  file.readlines()
    file.close()

    file = open(featuresFile,"r")
    features = file.readlines()
    file.close()

    file = open(nounsFile,"r")
    nouns = file.readlines()
    file.close()

    file = open (adjectivesFile,"r")
    adjectives = file.readlines()
    file.close()

    randomGenre01 = random.randrange(0,len(genres))
    randomGenre02 = random.randrange(0,len(genres))
    randomTheme01 = random.randrange(0,len(themes))
    randomTheme02 = random.randrange(0,len(themes))
    randomFeature01 = random.randrange(0,len(features))
    randomFeature02 = random.randrange(0,len(features))
    randomNoun = random.randrange(0,len(nouns))
    randomAdjective = random.randrange(0,len(adjectives))

    print(f"{Fore.GREEN}{Style.BRIGHT}" + "RUNNING IN DETAILED MODE: \n" + f"{Style.RESET_ALL}")

    print(f"{Fore.WHITE}{Style.BRIGHT}" + rules + f"{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{Style.BRIGHT}" + "Your random Genres are: " + f"{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{Style.BRIGHT}" + genres[randomGenre01] + genres[randomGenre02] + f"{Style.RESET_ALL}")

    print(f"{Fore.YELLOW}{Style.BRIGHT}" + "Your random Themes / moods are: " + f"{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{Style.BRIGHT}" + themes[randomTheme01] + themes[randomTheme02] + f"{Style.RESET_ALL}")

    print(f"{Fore.MAGENTA}{Style.BRIGHT}" + "Your random Features are: " + f"{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{Style.BRIGHT}" + features[randomFeature01] + features[randomFeature02] + f"{Style.RESET_ALL}")

    print(f"{Fore.RED}{Style.BRIGHT}" + "Your random word set is: " + f"{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{Style.BRIGHT}" + (adjectives[randomAdjective] + nouns[randomNoun]).title() + f"{Style.RESET_ALL}")

def GetTarget():
    print(f"{Fore.WHITE}{Style.BRIGHT}" + "Target:"+ f"{Style.RESET_ALL}")
    print("[1] Genres\n[2] Themes and Moods\n[3] Features\n[4] Nouns\n[5] Adjectives")
    target = int(input())
    file = None
    # 1. Genres 2. Themes 3. Features 4.Nouns 5. Adjectives
    if target == 1:
        return genresFile
    elif target == 2:
        return themesFile
    elif target == 3:
        return featuresFile
    elif target == 4:
        return nounsFile
    elif target == 5:
        return adjectivesFile
    else:
        print("Invalid target.")
        return GetTarget()

def TryAddElement(target):
    print(f"{Fore.WHITE}{Style.BRIGHT}" + "Input new element to add to target:"+ f"{Style.RESET_ALL}")
    newElement = input()
    checkElement = newElement + "\n"
    file = open(target,"r")
    currentElements = file.readlines()
    file.close()

    if checkElement.title() in currentElements:
        print(f"{Fore.RED}{Style.BRIGHT}" + "Element already exists in target!"+ f"{Style.RESET_ALL}")
    else:
        print("Adding new element: " + newElement + " to target.")
        file = open(target,"a")
        file.write(newElement.title() + "\n")
        file.close()

def RunAppendMode():
    target = GetTarget()
    TryAddElement(target)

def Main():
    title = "GameJam-Like Idea Generator v0.1\nby a quote unquote Dev\n"
    print(f"{Fore.GREEN}{Style.BRIGHT}" + title + f"{Style.RESET_ALL}")
    mode = int(GetMode())

    if mode == 1:
        print("\n")
        RunSimple()
    elif mode == 2:
        print("\n")
        RunDetailed()
    elif mode == 3:
        print("\n")
        RunAppendMode()


Main()
