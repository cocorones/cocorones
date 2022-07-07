import os
import random
import string
while True:
	letters = string.ascii_lowercase
print ( ''.join(random.choice(letters) for i in range(10)) )
os.mkdir(letters)