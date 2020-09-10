#password generator
,
#importing random module
import random

#ord() converts ascii character into ascii integer
#chr() converts ascii integer into ascii character

#getting input from user for max length
max=int(input("enter the max length of password \t: "))
print("\n max length is \t:"+ str(max))

#digits from 1 to 10
digit=[str(i) for i in range (10)]

#upper case letter list
upper_case=[chr(x) for x in range(ord('A'),ord('Z')+1)]

#lower case letter list
lower_case=[chr(y) for y in range(ord('a'),ord('z')+1)]

#symbols list
symbols=['@','$','!','&']

#combined all list
combined= digit+upper_case+lower_case+symbols

#getting random digit
rand_digit=random.choice(digit)

#getting random upper case letter
rand_upper=random.choice(upper_case)

#getting random lower case letter 
rand_lower=random.choice(lower_case)

#getting random symbol
rand_symbol=random.choice(symbols)


temp_password= rand_digit + rand_upper + rand_lower + rand_symbol

#looping for getting rest of the password
for k in range(max-4):
  temp_password= temp_password + random.choice(combined)


#print password
print(temp_password)


#password generatad










