import random
import string
letters=list(string.punctuation)+list(string.ascii_letters)+list(string.ascii_letters)
length=int(input('how long does the password have to be?'))
password=''
for x in range(0,length):
  password=password+(letters[random.randint(0,len(letters)-1)])
print(password)
