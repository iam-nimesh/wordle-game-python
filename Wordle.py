import random

def evaluate_guess(word, guesses):
    guess = []
    present_letters = set()

    for i in range(len(word)):
        if guesses[i] == word[i]:
            guess.append(guesses[i])
        elif guesses[i] in word:
            guess.append("_")
            present_letters.add(guesses[i])
        else:
            guess.append("_")

    return guess, present_letters


def main():
    while True:   

        words = ["TREND", "SPACE", "GREAT", "MANGO", "HELLO"]
        word = random.choice(words)
        attempts = 6

        print(f"Attempts remaining = {attempts}")

        while True:   
            guesses = input("Enter a 5 letter word: ").upper()

            if len(guesses) != len(word):
                print("Word must contain 5 letters!!")
                continue

            result, present_letters = evaluate_guess(word, guesses)

            print(" ".join(result))
            for letter in present_letters:
                print(f"{letter} is in the word")

            if "_" not in result:
                print("YOU GUESSED THE WORD!!!")
                break

            attempts -= 1
            if attempts == 0:
                print("Game Over!!!")
                break
            else:
                print(f"Attempts left = {attempts}")

       
        again = input("Play Again? (Y/N): ").upper()
        if again != "Y":
            break


if __name__ == "__main__":
    main()
