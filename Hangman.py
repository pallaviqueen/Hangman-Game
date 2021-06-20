import random
import os
import time 
import sys 
clear = lambda: os.system('cls')

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print('''
 _   _                                         
| | | |                                        
| |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  _  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
\_| |_/\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/       

''')

input("A python game developed by garfield#1234. Press enter to continue.")

clear()

file = open(os.path.join(sys.path[0], "words.txt"))
word_list = file.read().splitlines()
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

def thingy():
    print(stages[level])
    print(f"{' '.join(display)}")

won = True 
print(stages[6])
level = 6
print(f"{' '.join(display)}")

while won:
    Blocker = False 
    
    if level == 0:
        clear()
        print(stages[level])
        print("You've lost. The hangman has died.")
        time.sleep(1)
        input(f"\nThe word was '{''.join(chosen_word)}'.")
        break
    
    guess = input("\nGuess a letter: ").lower()

    if guess in display:
        level -= 1 
        clear()
        print("You've already guessed this letter.")
        Blocker = True 
        thingy()
        
    if Blocker == False: 
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
                clear()
                thingy()

    if guess not in chosen_word:
        clear()
        print("That letter is not in the word.")
        level -= 1 
        thingy()
    

    if "_" not in display:
        clear()
        print("You've won!")
        time.sleep(1)
        input(f"\nThe final word was {''.join(display)}.")
        break