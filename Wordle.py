word="SPACE"
guesses=input("Eter a 5 digit letter : ")
guess=[]
for i in range(len(word)):
    if guesses[i] == word[i]:
        guess.append(guesses[i])
    else:
        guess.append("_")
print(" ".join(guess))#Converts ["_", "_", "_", "_", "_"] to _ _ _ _ _

