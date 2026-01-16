#hang man game
import requests

#word bank from api
response = requests.get("https://random-words-api.kushcreates.com/api?language=en&category=programming_languages&type=lowercase&words=1")
data = response.json()
word = str(data[0]['word'])

word = [letter for letter in word] #convert word to list

hidden_word = ["_" for letter in word] #convert word to list

word_count = len(word)

#guesses
guesses = 6

while True:
    guess = input("letter count = " + str(word_count) + "\nguess left = " + str(guesses) + "\nGuess a letter: " + " " ).lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
    else:
        guesses -= 1

    print(" ".join(hidden_word))

    if "_" not in hidden_word:
        print("You win!")
        break

    if guesses == 0:
        print("You lose!, the word was " + str(word))
        break





