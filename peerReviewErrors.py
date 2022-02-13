# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <author>
# Creation Date: <date>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
    #To many quotations used and indented wrong
	print('You are in a land full of dragons. In front of you, you see two caves.In one cave, the dragon is friendly and will share his treasure with you. The other dragon is greedy and hungry, and will eat you on sight.')
	print()

def chooseCave():
    cave = ''
	while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
		cave = input()
        #return was improperly indented and cave has an 's' on the end
        return cave

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(2)
    #sleep had a 3 when it says sleep for 2 seconds
    
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
        #paraentheses were left off
		print ('Gobbles you down in one bite!')

playAgain = 'yes'
#equal sign missing from both playAgain tests
while playAgain == 'yes' or playAgain == 'y':
	displayIntro()
    #chooseCave function had lowercase 'C' instead of uppercase
	caveNumber = chooseCave()
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
    #does not contain the option for n like in the yes test above
	if playAgain == "no" or playAgain == 'n':
		print("Thanks for planing")

