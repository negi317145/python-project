#time tuple
import time
print(time.gmtime())

#formated time
import time
print(time.asctime())

#extract month
import datetime
d=datetime.date.today()
print(d.month)

#extract day 
import datetime
d=datetime.date.today()
print(d)
print(d.today)




#extract date from time
import datetime
d=datetime.date.today()
print(d.month)

#time using local time
import time
print(time.localtime())


#factorial of no.
import math
print(math.factorial(4))



#gcd of no.
import math 
a=int(input("enter A value-"))
b=int(input("enter B value-"))
print(math.gcd(a,b))



#operating system
import os
print(os.getcwd())
print(os.environ)