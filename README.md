# words-afet-G-g
Program: Words after "G"/"g" Create a program inputs a phrase (like a famous quotation) and prints all of the words that start with h-z  
Sample output:
WHERESOEVER
YOU
WITH
YOUR
HEART
split the words by building a placeholder variable: word

loop each character in the input string
check if character is a letter
add a letter to word each loop until a non-alpha char is encountered
if character is alpha

add character to word
non-alpha detected (space, punctuation, digit,...) defines the end of a word and goes to else
else
check if word is greater than "g" alphabetically
print word
set word = empty string
or else
set word = empty string and build the next word
Hint: use .lower()
