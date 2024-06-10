import random
from enwords_hangman import wordList

# HANGMAN GAME #

print("This is the Hangman Game.")
print("You have to guess the secret word before the man is hanged up.")

# GAME FUNCTION
def hangmanGame():

    # SECRET WORD SETTING
    word = random.choice(wordList)  # magic word
    print(f'The word is {len(word)} letters long.')
    word_to_list = [x for x in word]  # magic word to list

    undScores = ["_" for x in range(len(word))]
    print(undScores)

    # LETTERS INPUT AND "_" LIST FILL
    points = 5
    while points > 0:

        # LETTER INPUT WITH SECRET WORD COMPARISON
        myletter = input("Choose a letter: ")
        for idx, letter in enumerate(word):
            if letter == myletter:
                undScores[idx] = letter
        print(undScores)

        # POINTS SUBTRACTION
        if myletter not in word:
            points -= 1
            print("No such letter in the word")
            print(f'You have {points} points left')

        # ZERO POINTS LEFT
        if points == 0:
            print("You loose!")
            print(f'The secret word was "{"".join(word_to_list)}"')
            break

        # WIN CONDITION
        if undScores == word_to_list:
            print("You win!")
            print(f'The secret word is "{"".join(word_to_list)}"')
            break

hangmanGame()


# RESTART GAME
playAgain = input("Would you play again? [y/n]")
if playAgain == "y":
    hangmanGame()
elif print("Goodbye!"):
    stop()
