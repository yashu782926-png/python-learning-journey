print("Welcome to the Number Guessing Game!")
secret_number = int(input("Enter the secret number: "))
guess = int(input("Enter your guess: "))
while guess != secret_number:
  
 if guess < secret_number:
    print("Your guess is too low. Try again.")

 elif guess > secret_number:
    print("Your guess is too high. Try again.")
 else:
    print("Sorry, that's not the correct number.")
 guess = int(input("Enter your guess again: "))
print("Congratulations! You've guessed the correct number!")


attempts = 1
if guess != secret_number:
      attempts += 1
      print(f"You've made {attempts} attempts to guess the number.")

print("Thank you for playing the Number Guessing Game!")
