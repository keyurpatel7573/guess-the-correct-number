import random

a = random.randint(1,100)
i = -1
guesses = 1
while(i != a):
  i = int(input("Guess the number: "))
  if(i > a):
    print("Guess lower number")
    guesses += 1
  elif(i < a):
    print("Guess higher number")
    guesses += 1

print(f"You have guessed the number {a} correctly in {guesses} attempts")