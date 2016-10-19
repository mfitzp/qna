import random
import time

def display_grid(grid):
    #Task 2. Making the random words into a 3x3 grid
    grid = [words[i:i + 3] for i in range(0, len(words), 3)]
    for x,y,z in grid:
        print("%s %s %s" % (x.rjust(10), y.rjust(10), z.rjust(10)) ) 

def clear_screen():
    print("\n"*1000000)




#importing the word file and closing it automatically
#Task 1 and 2
with open("words.txt") as f:  
    wordlist = f.read().splitlines()
    
#Task 3. This creates another three by three grid from the file "words.txt"
words = random.sample(wordlist, 9)
display_grid(words)

#Thirty second timer before another action takes place
time.sleep(3)
clear_screen()

#Task 3. This creates another three by three grid from the file "words.txt"
words = random.sample(wordlist,9)

# Replace one of the words at random
i = random.randint(0,8)
replaced_word = words[i]
substituted_word = random.choice(wordlist)  # Get the random word
words[i] = substituted_word

#Making the random words into a 3x3 grid
display_grid(words)

#Thirty second timer before another action takes place
time.sleep(3)
clear_screen()

#Task 4 and task 5. Ask the user to guess the removed word.
userguess = str(input("What is the replaced word? ")).upper()
if userguess == replaced_word: 
    print("You have guessed correctly")
else:
    print("You have guessed incorrectly")

#Task 6. Ask the user to guess what the substitute word was.
userguess = str(input("what is the substituted word? ")).upper()
if userguess == substituted_word: 
    print("You have guessed correctly")
else:
    print("You have guessed incorrectly")
