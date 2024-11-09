import random

word_list = ["mosiah", "nephi", "helaman", "temple", "moroni"]
secret_word = random.choice(word_list)
guess_count = 0

print("Welcome to the word guessing game!")

while True:
    hint = '_' * len(secret_word)
    print("\nYour hint is:", ' '.join(hint))
    guess = input("What is your guess? ").strip().lower()
    
    guess_count += 1

    if len(guess) != len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word.")
        continue

    if guess == secret_word:
        print("Congratulations! You guessed it!")
        break

    hint = ''
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            hint += guess[i].upper()
        elif guess[i] in secret_word:
            hint += guess[i]
        else:
            hint += '_'

    print("Your hint is:", ' '.join(hint))

print(f"It took you {guess_count} guesses.")