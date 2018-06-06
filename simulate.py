import random

# A text-based simulator that outputs the final score of a simulated sports game

def main():
	while True:
		sport = input('Choose a sport:\n 1) Football\n 2) Basketball\n 3) Soccer\n 4) Quit\n Choice: ')
		if sport == "1": # Football
			matches = input('\nFootball! Enter the # of matches to simulate: ')
			try:
				if int(matches) <= 0:
					print("Error: # of matches must be a positive integer\n")		
				else:
					for match in range(1, int(matches)+1):
						homeFootballScore = random.randint(0,55) # Generate random scores for home/visitors
						visitorFootballScore = random.randint(0,55)
						print("Match " + str(match) + ": Home " + str(homeFootballScore) + " | Visitors " + str(visitorFootballScore))
						if homeFootballScore > visitorFootballScore:
							print("Home team wins!\n")
						elif homeFootballScore < visitorFootballScore:
							print("Visitors win!\n")
						elif homeFootballScore == visitorBasketballScore:
							print("Tie Game!\n")
			except ValueError:
				print("Error: # of matches must be a positive integer\n")
		elif sport == "2": # Basketball
			matches = input('\nBasketball! Enter the # of matches to simulate: ')
			try:
				if int(matches) <= 0:
					print("Error: # of matches must be a positive integer\n")	
				else:
					for match in range(1, int(matches)+1):
						homeBasketballScore = random.randint(75, 130)
						visitorBasketballScore = random.randint(75, 130)
						print("Match " + str(match) + ": Home " + str(homeBasketballScore) + " | Visitors " + str(visitorBasketballScore))
						if homeBasketballScore > visitorBasketballScore:
							print("Home team wins!\n")
						elif homeBasketballScore < visitorBasketballScore:
							print("Visitors win!\n")
						elif homeBasketballScore == visitorBasketballScore:
							print("Tie Game!\n")
			except ValueError:
				print("Error: # of matches must be a positive integer\n")
		elif sport == "3": # Soccer
			matches = input('\nSoccer! Enter the # of matches to simulate: ')
			try:
				if int(matches) <= 0:
					print("Error: # of matches must be a positive integer\n")					
				else: 
					for match in range(1, int(matches)+1):
						homeSoccerScore = random.randint(0,9)
						visitorSoccerScore = random.randint(0,9)
						print("Match " + str(match) + ": Home " + str(homeSoccerScore) + " | Visitors " + str(visitorSoccerScore))
						if homeSoccerScore > visitorSoccerScore:
							print("Home team wins!\n")
						elif homeSoccerScore < visitorSoccerScore:
							print("Visitors win!\n")
						elif homeSoccerScore == visitorSoccerScore:
							print("Tie Game!\n")
			except ValueError:
				print("Error: # of matches must be a positive integer\n")
		elif sport == "4": # Quit
			print("\nGoodbye")
			return False
		else:
			print("\nInvalid choice, pick again\n")
 
if __name__ == '__main__':
    main()
