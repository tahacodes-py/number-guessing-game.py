name = str(input("enter your name: "))
print("hello",name,"welcome to my number guessing game")
print("you have 4 chances to guess the number")
print("the number given wud be between 30 and 50")
import random
num1=random.randint(30,50)
for i in range(1,5):
  print("chance",i)
  num2=int(input("enter your guess: "))
  if num1==num2:
    print("you guessed it right congrats")
    break
  elif num2>num1:
    print("your guess is too high")
    print("try again")
  elif num2<num1:
    print("your guess is too low")
    print("try again")
else:
    print("Sorry, you're out of chances. The number was", num1)
