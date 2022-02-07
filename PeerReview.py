# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <author>
# Creation Date: <date>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.
#Author: Taylor Damron
#Date: 1/21/2021



import random
import time

def displayIntro():
  #9th Mistake - Text was indented wrong
	print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
  #1st Mistake - Improper indent
  cave = ''
  #2nd Mistake - Indents messed up
  while cave != '1' and cave != '2':
	  print('Which cave will you go into? (1 or 2)')
	  cave = input()
  
  #7th Mistake - cave not caves
  return cave

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
  #10th Mistake - Supposed to sleep for 2 seconds not 3
	time.sleep(2)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
    #3rd Mistake - Missing () on print
		print('Gobbles you down in one bite!')

playAgain = 'yes'
#4th and 5th Mistake - = is to set == is to compare
while playAgain == 'yes' or playAgain == 'y':
	displayIntro()
  #6th Mistake = chooseCave() not choosecave()
	caveNumber = chooseCave()
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no":
    #8th Mistake playing not planing
		print("Thanks for playing")

