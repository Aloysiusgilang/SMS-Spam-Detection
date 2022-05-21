from textColors import bcolors
from BM import BM
from KMP import KMP

adsSpam = open("adsSpam.txt", "r")
pornSpam = open("pornSpam.txt", "r")
virusSpam = open("virusSpam.txt", "r")
stopwords = open("stopwords-id.txt", "r")

adsSpamList = []
pornSpamList = []
virusSpamList = []
stopwordsList = []

for line in adsSpam:
    adsSpamList.append(line.strip())

for line in pornSpam:
    pornSpamList.append(line.strip())

for line in virusSpam:
    virusSpamList.append(line.strip())

for line in stopwords:
    stopwordsList.append(line.strip())

print("Input messagge : ")
message = input()
print("Select algorithm : ")
print("1. BM")
print("2. KMP")
algorithm = int(input())

# input preprocessing 
# tokenizing 
messageToken = message.split()

# case folding
messageToken = [word.lower() for word in messageToken]

# stopword removal
messageToken = [word for word in messageToken if word not in stopwordsList]

# spam detection
if algorithm == 1:
    print('\n');
    print(bcolors.OKCYAN + "SMS-Spam-Detection using BM algorithm:"+bcolors.ENDC + "\n")

    print ("Message : " + message + "\n")
    adsSpamCount = 0
    pornSpamCount = 0
    virusSpamCount = 0

    for word in messageToken:
        for adsSpamWord in adsSpamList:
            if (BM(word, adsSpamWord) == 1):
                adsSpamCount += 1
                break
        
        for pornSpamWord in pornSpamList:
            if (BM(word, pornSpamWord) == 1):
                pornSpamCount += 1
                break

        for virusSpamWord in virusSpamList:
            if (BM(word, virusSpamWord) == 1):
                virusSpamCount += 1
                break
    
    
    if adsSpamCount == 0 and pornSpamCount == 0 and virusSpamCount == 0:
        print(bcolors.BOLD + bcolors.OKGREEN +"Not spam" + bcolors.ENDC + bcolors.ENDC)
    elif adsSpamCount > pornSpamCount and adsSpamCount > virusSpamCount:
        print(bcolors.BOLD +bcolors.FAIL+ "Spam Detected" + bcolors.ENDC +  bcolors.ENDC)
        print(bcolors.WARNING +"Category : Ads Spam" + bcolors.ENDC)
    elif pornSpamCount > adsSpamCount and pornSpamCount > virusSpamCount:
        print(bcolors.BOLD +bcolors.FAIL+ "Spam Detected" + bcolors.ENDC +  bcolors.ENDC)
        print(bcolors.WARNING +"Category : Porn Spam" + bcolors.ENDC)

    elif virusSpamCount > adsSpamCount and virusSpamCount > pornSpamCount:
        print(bcolors.BOLD +bcolors.FAIL+ "Spam Detected" + bcolors.ENDC +  bcolors.ENDC)
        print(bcolors.WARNING +"Category : Virus Scam Spam" + bcolors.ENDC)


else :
    print('\n');
    print(bcolors.OKCYAN + "SMS-Spam-Detection using KMP algorithm:"+bcolors.ENDC + "\n")

    print ("Message : " + message + "\n")


    adsSpamCount = 0
    pornSpamCount = 0
    virusSpamCount = 0

    for word in messageToken:
        for adsSpamWord in adsSpamList:
            if (KMP(word, adsSpamWord) == 1):
                adsSpamCount += 1
                break
        
        for pornSpamWord in pornSpamList:
            if (KMP(word, pornSpamWord) == 1):
                pornSpamCount += 1
                break

        for virusSpamWord in virusSpamList:
            if (KMP(word, virusSpamWord) == 1):
                virusSpamCount += 1
                break
    
    
     
    if adsSpamCount == 0 and pornSpamCount == 0 and virusSpamCount == 0:
        print(bcolors.BOLD + bcolors.OKGREEN +"Not spam" + bcolors.ENDC + bcolors.ENDC)
    elif adsSpamCount > pornSpamCount and adsSpamCount > virusSpamCount:
        print(bcolors.BOLD +bcolors.FAIL+ "Spam Detected" + bcolors.ENDC +  bcolors.ENDC)
        print(bcolors.WARNING +"Category : Ads Spam" + bcolors.ENDC)
    elif pornSpamCount > adsSpamCount and pornSpamCount > virusSpamCount:
        print(bcolors.BOLD +bcolors.FAIL+ "Spam Detected" + bcolors.ENDC +  bcolors.ENDC)
        print(bcolors.WARNING +"Category : Porn Spam" + bcolors.ENDC)

    elif virusSpamCount > adsSpamCount and virusSpamCount > pornSpamCount:
        print(bcolors.BOLD +bcolors.FAIL+ "Spam Detected" + bcolors.ENDC +  bcolors.ENDC)
        print(bcolors.WARNING +"Category : Virus Scam Spam" + bcolors.ENDC)







