"""
Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει την διάσταση ενός τετραγώνου και
θα φτιάχνει μέσα από λίστες τον αντίστοιχο πίνακα.Στην συνέχεια θα βρίσκει το
πλήθος των θέσεων και θα γεμίζει στην τύχη τις μισές με μονάδες (στρογγυλοποίηση προς τα πάνω).
Σκοπός είναι να μετρήσετε πόσες τετράδες από μονάδες υπάρχουν οριζόντια, κάθετα, και διαγώνια.
Το πρόγραμμα επαναλλαμβάνεται 100 φορές (για την ίδια διάσταση) και επιστρέφει
τον μέσο όρο των τετράδων.
"""

import random
import math

#function used to check if the input is an integer higher than 3
def inputNumber(message):
	while True:
		try:
			userInput = int(input(message))
		except ValueError:
			print("Not an integer! Try again.")
			continue
		if userInput<4:
			print("The number is smaller than 4! Try again.")
			continue
		else:
			return userInput
			break

print("""
This programm calculates the average number (after 100 tries) of the 1111 quartets
in a NxN square table (horizontally, vertically and diagonally) where half of
the cells are filled with '1' randomly.
""")

n = inputNumber("Enter the dimensions of the square table (greater than 3): N = ")

cells = n**2
#print("The number of cells created are: ", cells)
h = float(cells/2)
m = math.ceil(h)
#print("Half of them rounded up are: ", m)

total = 0
for a in range(100):
	matrix = []
	for i in range(n):
		matrix.append([0] * n)

	#randomly sets the number 1 in half of the matrix cells
	sum = 0
	while sum<m:
		i = random.randint(0,n-1)
		j = random.randint(0,n-1)
		if matrix[i][j] == 0:
			matrix[i][j] = 1
			sum += 1

	#prints the matrix as a table (commented because table may be large)
	"""
	for i in range(n):
		for j in range(n):
			print(matrix[i][j], end = " ")
		print()
	"""

	#calculates horizontal quartets
	hor = 0
	horc = 0
	for i in range(n):
		for j in range(n-3):
			if matrix[i][j] == 1:
				for k in range(j,j+4):
					if matrix[i][k] == 1:
						hor += 1
						if hor == 4:
							horc += 1
							hor = 0
					else:
						hor = 0
			else:
				hor = 0
		hor = 0
	#print("The horizontal quartets are: ", horc)


	#calculates vertical quartets
	ver = 0
	verc = 0
	for j in range(n):
		for i in range(n-3):
			if matrix[i][j] == 1:
				for k in range(i,i+4):
					if matrix[k][j] == 1:
						ver += 1
						if ver == 4:
							verc += 1
							ver = 0
					else:
						ver = 0
			else:
				ver = 0
		ver = 0
	#print("The vertical quartets are: ", verc)


	#calculates diagonal quartets from left to right
	diar = 0
	diarc = 0
	for i in range(n-3):
		for j in range(n-3):
			if matrix[i][j] == 1:
				p = j
				for k in range(i,i+4):
					if matrix[k][p] == 1:
						diar += 1
						p += 1
						if diar == 4:
							diarc += 1
							diar = 0
					else:
							diar = 0
			else:
				diar = 0
		diar = 0
	#print("The diagonal quartets from left to right are: ", diarc)


	#calculates diagonal quartets from right to left
	dial = 0
	dialc = 0
	for i in range(n-3):
		for j in range(3,n):
			if matrix[i][j] == 1:
				p = j
				for k in range(i,i+4):
					if matrix[k][p] == 1:
						dial += 1
						p -= 1
						if dial == 4:
							dialc += 1
							dial = 0
					else:
						dial = 0
			else:
				dial = 0
		dial = 0
	#print("The diagonal quartets from right to left are: ", dialc)

	total = total + horc + verc + diarc + dialc

#print("The total 1111 quartets found are: ", total)
average = total/100
print("""
The average number of 1111 quartets found in 100 %dx%d tables is: """ %(n, n), average)
