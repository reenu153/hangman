#This is a simple game of hangman
print(" *	*       *     	*      * ******** *     *       *      *     * ")
print("	*	*      * *      * *    * *	  **   **      * *     **    * ")
print("	*	*     *   * 	*  *   * *	  * * * *     *   *    * *   * ")
print("	  *****      ******* 	*   *  * *	  *  *  *    *******   *  *  * ")
print("	*	*   *       *   *    * * *  ***** *     *   *       *  *   * * ")
print("	*	*  *	     *  *     ** *      * *     *  *         * *    ** ")
print("	*	* *	      * *      * ******** *     * *           **     * ")
 

import random
	
def hang(trial):
	if trial==9:
		print(" ----")
		print("   | ")
		print("   O ")
		print("  /|\\")
		print("   | ")
		print("  / \\")
	elif trial==8:
		print("   | ")
		print("   O ")
		print("  /|\\")
		print("   | ")
		print("  / \\")
	elif trial==7:
		print("   O ")
		print("  /|\\")
		print("   | ")
		print("  / \\")
	elif trial==6:
		print("   O ")
		print("  /|\\")
		print("   | ")
		print("  /  ")
	elif trial==5:
		print("   O ")
		print("  /|\\")
		print("   | ")
	elif trial==4:
		print("   O ")
		print("  /| ")
		print("   | ")
	elif trial==3:
		print("   O ")
		print("   | ")
		print("   | ")
	elif trial==2:
		print("   O ")
		print("   | ")
	elif trial==1:
		print("   O ")
	return
ch= input("Enter the category \n1.Movie \n2.Country \n3.TVShow \n4.Book\n")
movie=["unstoppable","harry potter","die hard","miss congeniality","the terminal","lethal weapon","dirty dozen"]
country=["south korea","japan","qatar","switzerland","germany","ireland","bangladesh","nepal"]
tvshow=["agents of shield","cloak and dagger","game of thrones","teen wolf","the flash","pretty little liar"]
book=["inferno","angels and demons","the davinci code","heroes of olympus","percy jackson","the book theif"]

if ch=='1':
	word=random.choice(movie)
elif ch=='2':
	word=random.choice(country)
elif ch=='3':
	word=random.choice(tvshow)
elif ch=='4':
	word=random.choice(book)
else:
	print("invalid entry")
guess=''
k=0
for i in word:
	if i==' ':
		guess=guess+' '
	else:
		guess=guess+'_'
	k=k+1
print ("your word is "+ guess)
trial=0
flag=0;
while(trial<=9):
	g=input("\nGuess a letter or the word ")
	if len(g)==1 and g not in word:
		trial=trial+1
		hang(trial)
	elif g!=word:
		trial=trial+1
		hang(++trial)
	elif g==word:
		print ("\nCongratulations!! You guessed the word right")
		break;
	elif len(g)==1 and g in word:
		for i in range(len(word)):
			if word[i]==g:
				guess=guess[:i-1]+'g'+guess[i+1:]
		print ("You guessed right! Your word is\n "+ guess)
