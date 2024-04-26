# 1. Import modulu random
import random

# 2. Vygenerování náhodného 4 místného čísla
def generate_secret_number():
    digits = list(range(1, 10))  
    random.shuffle(digits)  
    return ''.join(map(str, digits[:4]))

# 3. Pozdravení a úvodní text
def generate_greeting():
    greeting = "Hi there!"
    text_a = "I've generated a random 4 digit number for you."
    text_b = "Let's play a bulls and cows game."
    separator = "-" * len(text_a)
    return f"{greeting}\n{separator}\n{text_a}\n{text_b}\n{separator}"    
print(generate_greeting())

def evaluate_guess(secret_number, guess):
    """Vygeneruje počet bullů a cows."""
    bulls = sum(1 for x, y in zip(secret_number, guess) if x == y)  # Bull = správné číslo na správné pozici
    cows = sum(1 for x in guess if x in secret_number) - bulls  # Cow = správné číslo na nesprávné pozici
    return bulls, cows

# 4. Vložení 4 místního čísla
def main():
    secret_number = generate_secret_number()
    print(generate_greeting())
    guesses = 0
    while True:
        guess = (input("Enter a number:\n"))
        # Kontrola správnosti vstupu
        if not guess.isdigit() or len(guess) != 4 or guess[0] == '0'or len(set(guess)) != 4:
            print("Invalid input. Please enter a 4-digit number with unique digits and without leading zeros.")
            continue

        guesses += 1
        bulls, cows = evaluate_guess(secret_number, guess)

        if bulls == 4:
            print(f"Correct, you've guessed the right number in {guesses} guesses!")
            break
        else:
            print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, {cows} {'cow' if cows == 1 else 'cows'}")

    while True:
        next_game = input("Do you want to play next game? (y/n): ")
        if next_game.lower() == "n":
            print("Goodbye!")
            break
        elif next_game.lower() != "y":
            print("Invalid input. Please enter 'y' or 'n'.")
            continue
        else:
            main()

if __name__ == "__main__":
    main()