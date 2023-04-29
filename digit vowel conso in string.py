numOfWords=1
numOfDigits=0
numOfLetters=0
text=input("Enter text:")
for x in text:
    x.lower()
    if x>='a' and x<='z':
        numOfLetters=numOfLetters+1
    elif x>='0' and x<='9':
        numOfDigits=numOfDigits+1
    elif x==" ":
        numOfWords=numOfWords+1
print("numOfWords",numOfWords)
print("numOfDigits",numOfDigits)
print("numOfLetters",numOfLetters)
