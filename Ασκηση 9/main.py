'''
Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει σαν είσοδο ένα αρχείο
ASCII κειμένου και μετατρέπει τον κάθε χαρακτήρα στον αντίστοιχο αριθμό
ASCII και κρατάει τους μονούς. Εμφανίστε τα στατιστικά εμφάνισης του κάθε
γράμματος με “μπάρες” χρησιμοποιώντας το χαρακτήρα *, όπου κάθε * αντιστοιχεί σε 1%.
Η στρογγυλοποίηση θα γίνει προς τα πάνω.
'''

import math

n = input("Enter the name of the .txt file you wish to search: ")
q = open(n, "r")
x = q.read()

print(x)


#Converts the text to ASCII
ASCII = []
for word in x:
    ASCII_number = ord(word)
    ASCII.append(ASCII_number)
print(ASCII)

#Transfers odd numbers to another list
odds =[]
for i in range(len(ASCII)):
    if ASCII[i] % 2 == 1:
        odds.append(ASCII[i])
print(odds)

length_of_text = len(odds)

#Calculates the percentage of each number in the odds list
perc = {}
for i in odds:
    a = odds.count(i)
    b = math.ceil(a/length_of_text*100)
    perc.update({chr(i):b})
print(perc)

keys_list = perc.keys()

for w in keys_list:
    x = perc.get(w) * "*"
    print("The percentage of {} in * is:".format(w), x)
