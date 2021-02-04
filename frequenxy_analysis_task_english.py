import random
import string


secret_message = "VG HFRQ GB OR RKCRAFVIR GB ZNXR GUVATF CHOYVP NAQ PURNC GB ZNXR GURZ CEVINGR ABJ VGF RKCRAFVIR GB ZNXR GUVATF CEVINGR NAQ PURNC GB ZNXR GURZ CHOYVP"
frict = {}
for c in secret_message:
    if c in frict.keys():
        frict[c] += 1
    else:
        frict[c] = 1
sorted_frict = {k:v for k,v in sorted(frict.items(), key=lambda x: x[1], reverse=True)}
sorted_frict.pop(' ')
real_letters = "etaoinshrdlcumwfgypbvkjxqz"

sorted_frict ={
 'R': ['e'],
 'G': ['t'],
 'V': ['i'],
 'N': ['a'],
 'C': ['p'],
 'A': ['n'],
 'F': ['s'],
 'B': ['o'],
 'Z': ['m'],
 'U': ['h'],
 'I': ['v'],
 'X': ['k'],
 'P': ['c'],
 'H': ['u'],
 'Q': ['d'],
 'O': ['b'],
 'K': ['x'],
 'T': ['g'],
 'Y': ['l'],
 'E': ['r'],
 'J': ['w']}
alfabet = list(string.ascii_lowercase)
secret_message_list = list(secret_message)
for i in range(len(secret_message_list)):
    if secret_message_list[i] in sorted_frict.keys():
        random_letter = random.choice(sorted_frict[secret_message_list[i]])
        secret_message_list[i] = random_letter
print("".join(secret_message_list))
print()
print(secret_message.split())