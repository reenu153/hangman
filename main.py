print   *	*	*	*      * ******** *     *       *      *     *
print	*	*      * *	* *    * *	  **   **      * *     **    *
print	*	*     *   * 	*  *   * *	  * * * *     *   *    * *   *
print	*********    ******* 	*   *  * *	  *  *  *    *******   *  *  *
print	*	*   *       *   *    * * *  ***** *     *   *       *  *   * *
print	*	*  *	     *  *     ** *      * *     *  *         * *    **
print	*	* *	      * *      * ******** *     * *           **     *
 
print "\n WELCOME TO HANGAN \n YOU HAVE TO GUESS THE WORD IN 9 OR LESS TRIALS \n              GOOD LUCK!"
import random
def hang(trial):
	if trial==9:
		print" ----"
		print"   | "
		print"   O "
		print"  /|\"
		print"   | "
		print"  / \"
	if trial==8:
		print"   | "
		print"   O "
		print"  /|\"
		print"   | "
		print"  / \"
	if trial==7:
		print"   O "
		print"  /|\"
		print"   | "
		print"  / \"
	if trial==6:
		print"   O "
		print"  /|\"
		print"   | "
		print"  /  "
	if trial==5:
		print"   O "
		print"  /|\"
		print"   | "
	if trial==4:
		print"   O"
		print"  /|"
		print"   |"
 	if trial==3:
		print"   O"
		print"   |"
		print"   |"
	if trial==2:
		print"   O"
		print"   |"
	if trial==1:
		print"   O"
 	return
ch=input("Enter the category \n1.Movie \n2.Country \n3.TVShow \n4.Book")
movie=["unstoppable","harry potter","die hard","miss congeniality","the terminal","lethal weapon","dirty dozen"]
country=["south korea","japan","qatar","switzerland","germany","ireland","bangladesh","nepal"]
tvshow=[""agents of shield","cloak and dagger","game of thrones","teen wolf","the flash","pretty little liar"]
book=["inferno","angels and demons","the davinci code","heroes of olympus","percy jackson","the book theif"]

if ch==1:
	word=random.choice(movie)
elif ch==2:
	word=random.choice(country)
elif ch==3:
	word=random.choice(tvshow)
elif ch==4:
	word=random.choice(book)
else:
	print"invalid entry"

guess=word
print "your word is ",
for i in word:
	if i==" ":
		print " "
	else:
		print "_"

for i in range(len[word]):
	if word[i]==" ":
		guess[i]=" "
	else:
		guess[i]="_"
trial=0
got=0
while(trial<=9):
	g=raw_input("Guess a letter or the word")
        if g.isalpha==True and 
	
