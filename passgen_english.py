import random
letters=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','i','j','k','l','z','x','c','v','b','n','m','1','2','3','4','5','6','7','8','9','0']
length=int(input('how long does the password have to be?'))
a=0
password=''
while a<length:
  password=password+(letters[random.randint(0,len(letters)-1)])
  a=a+1
print(password)