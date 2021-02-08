'''
Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει σαν είσοδο ένα αρχείο ASCII κειμένου,
το χωρίζει σε λέξεις και εμφανίζει τα ζευγάρια λέξεων όπου το συνολικό τους
μήκος χαρακτήρων είναι 20. Κάθε ζευγάρι φεύγει από το σύνολο και το πρόγραμμα
τελειώνει όταν εξαντληθούν τα ζευγάρια.
'''
import re
import string

print("\n")
n = input("Enter the name of the .txt file you wish to search: ")
q = open(n, "r", encoding="utf-8")
text = q.read()


#Splits the ASCII text into words and puts them in a list
slst = text.split()
sum = 20

#Removes all the punctuation
for i in range(len(slst)):
    slst[i] = slst[i].translate(str.maketrans('', '', string.punctuation))

counter = 0
results = []
slst.sort(key=len)
(low, high) = (0, len(slst) - 1)
while low < high:
    if len(slst[low])  + len(slst[high]) == sum:
        counter += 1
        results.append(slst[low]), results.append(slst[high])
        slst[low] = ''
        slst[high] = ''
        high -= 1
        low += 1
    elif len(slst[low]) + len(slst[high]) < sum:
        low += 1
    else:
        high -= 1

z = 1
if counter == 0:
    print("\n No pairs were found.")
else:
    print("\n",counter, "pairs were found: \n")
    for i in range(0, len(results), 2 ):
        print(z,'.', results[i], results[i+1])
        z += 1
