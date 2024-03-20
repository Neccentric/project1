# Write a Program that prints Even Numbers from 1 to 10.
Even_Numbers = 2
while Even_Numbers <= 100 and Even_Numbers % 2 == 0:
    print(Even_Numbers)
    Even_Numbers += 2
# Program that prints Numbers from 1 to 20 but prints 6 and 10 in words.
for i in range(1,21):
    if i == 6:
        print("Six")
    elif i == 10:
        print("Ten")
    else:
        print(i)
# A Program that inputs a letter from the User and determines if the letter is a 'Vowel' or 'consonant'.
letter = input("Enter a letter: ")  
if len(letter) == 1 and letter.isalpha():
    letter = letter.lower()
    if letter in['a','e','i','o','u']:
        print(f"{letter} is a Vowel.")
    else:
        print(f"{letter} is a Consonant.")
else:
        print("Please enter a valid single letter.") 
        # Squares and Cubes of NUmbers from 1 to 9 using a FOR or WHILE LOOP.
print("Using a FOR LOOP:")
for i in range(1,10):
    square = i*i
    cube = i*i*i
    print(f"Number {i}: Square is {square}, Cube is {cube}")
        