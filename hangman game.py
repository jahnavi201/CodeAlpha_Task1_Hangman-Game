import random

# List of words
words = ["apple", "banana", "grape", "mango", "peach", "orange", "cherry"]

# Choose random word
word = random.choice(words)

guessed_letters = []
attempts = 6

print("🎮 Welcome to Hangman Game!")

# Game loop
while attempts > 0:
    display = ""

    # Display word with guessed letters
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check if player won
    if "_" not in display:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    try:
        guess = input("Enter a letter: ").lower()
    except KeyboardInterrupt:
        print("\nGame stopped by user.")
        break

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❗ Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print("✅ Correct guess!")
    else:
        attempts -= 1
        print("❌ Wrong! Attempts left:", attempts)

# If player loses
if attempts == 0:
    print("\n💀 Game Over! The word was:", word)