import random
n = random.randint(1, 30)
print("Welcome to the guess the Number game!!!")
print("\n Select a number between 1 to 30")

guess_number=int(input('\n please Enter any number:'))

while n!= guess_number:
  if guess_number< n:
     print(" This Number is too small!!")
     guess_number=int(input("Enter a bigger number from previous one:"))
  elif guess_number>n:
      print(" This Number is too Bigg!!")
      guess_number=int(input("Enter a smaller number from previous one:"))
  else:
     break
print("yeah!!!! you got it right!!!!!")