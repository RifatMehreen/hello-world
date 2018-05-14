import random

possibleans = ["PYTHON", "CSS", "COBOL", "JAVA", "JAVASCRIPT", "LARAVEL", "HTML", "RUBY", "ACTIONSCRIPT"]

random.shuffle(possibleans)

ans = list(possibleans[0])

display = []
display.extend(ans)

for i in range(len(display)):
	display[i] = "_"

print ("The topic is: Programming languages\n\n")

print("Total length of the word "+str(len(ans)))

print ' '.join(display)
print "\n\n\n\n"

count = 0


while count < len(ans):
	guess = raw_input("Please guess a letter:   ")
	guess = guess.upper()
	
	for i in range(len(ans)):
		if ans[i] == guess:
			display[i] = guess
			count += 1
	print("you have guessed: " + str(count) + " correct letters\n")
	print ' '.join(display)
	print "\n\n\n"
	
	
print "You guessed it!"
		
