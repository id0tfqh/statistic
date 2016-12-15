# http://www.itmathrepetitor.ru/prog/zadachi-na-vychisleniya/
### zadachi-na-vychisleniya 

#1
print ('#1')
print ('"Silence is golden"')
print (' ')

#2
print ('#1')
list = ['sreda', 'august', 'refi3489jffff' ]
for t in list:
    print(t)
print (' ')

#3
print ('#2')
q = 1
while q < 6:
    print (q*'0')
    q = q + 1
print (' ')

#4
print ('#4')
a = '    AAAAAAA'
q = 1
while q < 6:
    print (a)
    q = q + 1
print (' ')

#5
print ('#5')

print ('*     *     *')
print (' *   * *   *')
print ('  * *   * *')
print ('   *     *')

print (' ')

#6
print ('#6')
print (1+2-4)
print (' ')

#7
print ('#7')
print (1./2. + 1./4.)
print (' ')

#8
print ('#8')
a = 2; b = 3
print ((a + 4*b)*(a - 3*b) + a*a)
print (' ')

#9
print ('#9')
x = lambda x: abs(x)+x**5
print (' ')

#10
print ('#10')
x = lambda x: (x+1)**2 + 3*(x+1)
x(1.7)
x(3)
print (' ')

#11
print ('#11')
import math
x = lambda x: (abs(x-5)-math.sin(x))/3+(math.sqrt(x**2+2014))*math.cos(2*x)-3
x(-2.34)
print (' ')

#12
print('#12')
import math
x = lambda x: math.exp(x-2) + math.fabs(math.sin(x)) - math.pow(x, 10)*math.cos(1/x)
x(3.6)
print (' ')

#13
print('#13')
import math
x = lambda a,b,x: math.pow(x**2+b, 0.2) - ((b**2)*(math.sin(x+a))**3)/x
x(0.1,0.2 ,1)
print (' ')

#14
print('#14')
while 1:
    try:
        a = float (raw_input('input numer1:'))
        break
    except(TypeError, ValueError):
        print ('Input is number')

while 1:
    try:
        b = float (raw_input('input numer2:'))
        break
    except(TypeError, ValueError):
        print ('Input is number')

sum = a + b; print (sum)
pow= a*b; print(pow)
print (' ')

#15
print('#15')
while 1:
    try:
        a = float (raw_input('input numer1:'))
        break
    except(TypeError, ValueError):
        print ('Input is number')

double = a**2; print(double)
trea = a**3; print(trea)
print(' ')

#16
print('#16')
while 1:
    try:
        a = float (raw_input('input numer1:'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        b = float (raw_input('input numer2:'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        c = float (raw_input('input numer3:'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
a = a*2; b = b-3; c = c**2
print(a+b+c)
print(' ')

#17
print('#17')
while 1:
    try:
        a = float (raw_input('input numer1:'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        b = float (raw_input('input numer2:'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        c = float (raw_input('input numer3:'))
        break
    except(TypeError, ValueError):
        print ('Input is number')

av = 'average =  ' + repr((a+b+c)/3); print av
bxz = 'wers = ' + repr(2*(a+c)-c*3); print bxz
print (' ')

#18
print('#18')
while 1:
    try:
        a = float (raw_input('input the size a side:'))
        break
    except(TypeError, ValueError):
        print ('Input is number')

perimetr = 'Perimetr = ' + repr(a*4); print perimetr
square = 'Square = ' + repr(a**2); print  square
print (' ')

#19
print('#19')
while 1:
    try:
        a = float (raw_input('input price of candy:'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        b = float (raw_input('input price of coockies:'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
purchase1 = '300 gr candy and 400 gr coockies = ' + repr(0.3*a + 0.4*b)
purchase2 = '3 purchase on 2 kg coockies and 1.8 kg candy = ' + repr(3*(2*b + 1.8*a))
print purchase1
print purchase2
print(' ')

#20
print('#20')
while 1:
    try:
        a = float (raw_input('input time (minuts):'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        b = float (raw_input('input distance (kilometers):'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
rate = 'rate (meter/seconds) = ' + repr(0.06*b/a); print rate
print(' ')

#21
print('#21')
import math as m
while 1:
    try:
        a = float (raw_input('input leg a :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        b = float (raw_input('input leg b :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
squere = ' Squere = ' + repr(a*b/2)
hypotenuse = ' Hypotenuse = ' + repr(m.sqrt(a**2 + b**2))
perimeter = ' Perimeter = ' + repr(a + b + m.sqrt(a**2 + b**2))
print squere; print perimeter; print hypotenuse
print(' ')

#22
print('#22')
while 1:
    try:
        t = float (raw_input('input temperature Celsion :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
farengate = 'Farengate temperature = ' + repr(t*9/5+32)
print farengate
print(' ')

#23
print('#23')
while 1:
    try:
        x = float (raw_input('input  weight of candy :'))
        if x <= 0:
            print ('Input is correct number')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')
   
while 1:
    try:
        a = float (raw_input('input price of candy :'))
        if a <= 0:
            print ('Input is correct number')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')

while 1:
    try:
        y = float (raw_input('input  new weight of candy :'))
        if y <= 0:
            print ('Input is correct number')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        k = float (raw_input('input  how many money :'))
        if k <= 0:
            print ('Input is correct number')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
 Y = 'Quantity of candy = ' + repr(a*y/x); print Y
 K = 'Quantity of money = ' + repr(k*x/a); print K
print(' ')

#24
print('#24')
while 1:
    try:
        baks = int(raw_input('input  how many money :'))
        if baks <= 0:
            print ('Input is correct number')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        d = int(raw_input('input  how many day :'))
        if d <= 0:
            print ('Input is correct number')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        s = float(raw_input('input sale in percent:'))
        if s < 0:
            print ('Input is correct number')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
cimes = 'Profit = ' + repr(float(baks + d*3)*(1 + s/100)); print cimes
print(' ')

#25
print('#25')
while 1:
    try:
        weeks = int(raw_input('input number of weeks :'))
        if weeks <= 0:
            print ('Input is correct number')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        months = int(raw_input('input enter number of months :'))
        if months <= 0:
            print ('Input is correct number')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        years = int(raw_input('input enter number of years :'))
        if years <= 0:
            print ('Input is correct number')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
number = 'Number of days = ' + repr(weeks*7 + 30*months + 365*years)
print number
print(' ')

#26
print('#26')
a = raw_input('input data 1 :')
b = raw_input('input data 2 :')
data_1 = 'Varible a = ' +repr(a)
data_2 = 'Varible b = ' +repr(b)
print data_1; print data_2
a,b = b,a
data_1 = 'Varible a = ' +repr(a)
data_2 = 'Varible b = ' +repr(b)
print data_1; print data_2
print(' ')

#27
print('#27')
while 1:
    try:
        a = float(raw_input('input nymber varible a :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')

while 1:
    try:
        b = float(raw_input('input nymber varible b :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')

while 1:
    try:
        c = float(raw_input('input nymber varible c :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        

data_1 = 'Varible a = ' +repr(a); print data_1
data_2 = 'Varible b = ' +repr(b); print data_2
data_3 = 'Varible c = ' +repr(c); print data_3

data_1 = 'New varible a = a + b = ' + repr(a + b); print data_1
data_2 = 'New varible b = c - a = ' + repr(c - a); print data_2
data_3 = 'New varible c = a + b + c = ' + repr(c + a + b); print data_3
print(' ')

#28
print('#28')
while 1:
    try:
        c = float(raw_input('input nymber cache :'))
        if c <= 0:
            print ('Input is correct number')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')

while 1:
    try:
        p = float(raw_input('input nymber percent :'))
        if p <= 0:
            print ('Input is correct number')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
years = float(5)
summa = 'Deposit over five years = ' + repr(c + years * (c*p/100))
print summa
print(' ')

#29
print('#29')
q = raw_input('input :'); w = raw_input('once again :')
print q; print w
q, w = w, q
print q; print w
print(' ')

# 30
print('#30')
while 1:
    try:
        r = float(raw_input('input real part of number a :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')

while 1:
    try:
        c = float(raw_input('input complex part of number a :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
a = complex(r, c)
a = a*a; a = a*a
a4 = 'a^4 = ' + repr(a); print a4

a = complex(r, c)
a = a*a*a; a = a*a
a6 = 'a^6 = ' + repr(a); print a6

a = b = complex(r, c)
a = a*a; a = a*a; b = b*a; b=b*b*b
a15 = 'a^15 = ' + repr(b); print a15
print(' ')

#31
print('#31')
a = 647
b = 170
qwadr = 30
number = 'Number square = ' + repr(int(a*b/qwadr)); print number
print(' ')

#32
print('#32')
d = 237
c = d//100; ab = d%(c*100)
x = 'Required number = ' + repr(10*ab + c); print x
print(' ')

#33
print('#33')
import math as m
while 1:
    try:
        x = float(raw_input('input nymber x :'))
        if y < 0:
            print ('Input is correct number')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        y = float(raw_input('input nymber y :'))
        if y < 0:
            print ('Input is correct number')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')

try:
    root = m.sqrt(x - m.sqrt(y))
except(ValueError):
    print('sqrt(y) > x'); root = 'Unconfined'
        
print root
print(' ')

#34
print('#34')
import random
i = random.randint(1,40)

for n in xrange(0,i):
    c = random.gammavariate(1, 5)
    if c > 3: c = c + 10
    else: c = c - 10
    print c
    
print(' ')

#35
print('#35')
import random
i = random.randint(1,40)

for n in xrange(0,i):
    c = random.gammavariate(1, 5)
    if c < 7: print ('Yes')
    elif c > 10: print ('No')
    elif c == 9: print ('Error')
    print c
    
print(' ')

#36
print(#'36')

while 1:
    try:
        x = int(raw_input('input nymber month :'))
        if x <= 0: print ('Input is correct number month')
        elif x > 12: print ('Input is correct number month')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
months = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun',
          7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}

for key, value in months.items():
    if key == x:
        print(value)
print(' ')

#37
print('#37')
import random

n = random.gammavariate(1, 800.052)
m = random.gammavariate(1, 400.752)

if abs(n-m) > 0: print (n)
else: print (m)
print(' ')


#38
print('#38')
import random

n = random.gammavariate(1, 800.052)
m = random.gammavariate(1, 400.752)

if abs(n-m) > 0: print ('yes')
else: print ('No')
print(' ')

#39
print('#39')
import random

n = random.gammavariate(1, 1.751)
Varible_1 = 'Varible_1 = ' + repr(n); print(Varible_1)
m = random.gammavariate(1, 1.752)
Varible_2 = 'Varible_2 = ' + repr(m); print(Varible_2)

if n-m > 0: print ('yes')
else: 
    n,m = m,n
    Varible_1 = 'Varible_1 = ' + repr(n); print(Varible_1)
    Varible_2 = 'Varible_2 = ' + repr(m); print(Varible_2)
    
print(' ')

#40
print('#40')
import random
m = random.uniform(-100, 100)
number = 'Number = ' + repr(m); print (number)

if 10 > m >= (-10):
    m = m + 5
    number = 'Number = ' + repr(m); print (number)
else:
    m = m -10
    number = 'Number = ' + repr(m); print (number)
    
print(' ')

#41
print('#41')
import random
m = random.uniform(-200, 200)
number = 'Number = ' + repr(m); print (number)

if m > 100 or m < -100:
    m = 0
else: m = m + 1

number = 'Number = ' + repr(m); print (number)
print(' ')

#42
print('#42')
import random
n = random.uniform(-10, 5000)
number = 'Number = ' + repr(n); print (number)

if 5 >= n > 2:
    n = n + 10
    number = 'Number = ' + repr(n); print (number)
elif 40 > n > 7 :
    n = n - 100
    number = 'Number = ' + repr(n); print (number)
elif 0 > n or 3000 < n :
    n = n*3
    number = 'Number = ' + repr(n); print (number)
else:
    n = 0
    number = 'Number = ' + repr(n); print (number)
    
print(' ')

#43
print(' ')

while 1:
    try:
        x = int(raw_input('input nymber month :'))
        if x <= 0: print ('Input is correct number month')
        elif x > 12: print ('Input is correct number month')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')

if 5 >= x >= 3 : print('Spring')
elif 8 >= x >= 6 : print('Summer')
elif 11 >= x >= 9 : print('Autumn')
elif 1 <= x <=2 or x == 12: print ('Winter')

print(' ')

#44
print('#44')
while 1:
    try:
        c = int(raw_input('input number_1 :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        d = int(raw_input('input number_2 :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
if c%2 != 0 and c != 10 and d != 10:
    number = 'Number = ' + repr(c + d); print (number)
    
else: number = 'Number = ' + repr(c * d); print (number)
print(' ')

#45
print('#45')
while 1:
    try:
        c = int(raw_input('input number_1 :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        d = int(raw_input('input number_2 :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        e = int(raw_input('input number_3 :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
if c > 10 and d > 10 and e > 10 and c%3 == 0 and d%3 == 0:
    print ('Yez')
else: print 'No'
print (' ')

#46
print('#46')
while 1:
    try:
        c = int(raw_input('input number_1 :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        d = int(raw_input('input number_2 :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        e = int(raw_input('input number_3 :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')

if c%5 != 0 and d%5 != 0 and e%5 != 0:
    print 'Error'
        
if c%5 != 0: c = 0
elif d%5 != 0: d = 0
elif e%5 != 0: e = 0; print (c + d + e)

print(' ')

#47
print('#47')
import random

n = random.gammavariate(1, 1.751)
Varible_1 = 'Varible_1 = ' + repr(n); print(Varible_1)
m = random.gammavariate(1, 1.752)
Varible_2 = 'Varible_2 = ' + repr(m); print(Varible_2)
b = random.gammavariate(1, 1.750)
Varible_3 = 'Varible_3 = ' + repr(b); print(Varible_3)

if n > m and n > b:
    print 'n is big'
elif m > n and m > b:
    print 'm is big'
elif b > n and b > m:
    print 'b is big'
    
print (' ')

#48
print('#48')
import random

n = random.uniform(-10, 10)
Varible_1 = 'Varible_1 = ' + repr(n); print(Varible_1)
m = random.uniform(-10, 10)
Varible_2 = 'Varible_2 = ' + repr(m); print(Varible_2)
b = random.uniform(-10, 10)
Varible_3 = 'Varible_3 = ' + repr(b); print(Varible_3)

if n+m > m+b and n+m > n+b:
    print 'n and m is big'
elif m+b > m+n and m+b > n+b:
    print 'm and b is big'
elif b+n > n+m and b+n > m+b:
    print 'b and n is big'
    
print(' ')

#49
print('#49')
while 1:
    try:
        c = int(raw_input('input number_1 :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        d = int(raw_input('input number_2 :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        e = int(raw_input('input number_3 :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        f = int(raw_input('input number_4 :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')

if c%2 != 0:
    c = 0
elif d%2 != 0:
    d = 0
elif e%2 != 0:
    e = 0
elif f%2 != 0:
    f = 0

if c > d and c > e and c > f:
    print 'c is big'
elif d > c and d > e and d > f:
    print 'd is big'
elif e > d and e > c and e > f:
    print 'e is big'
elif f > d and f > e and c < f:
    print 'f is big'
else: 'not found'
    
print(' ')

#50
print('#50')
import random

n = random.uniform(-10, 10)
Varible_1 = 'Varible_1 = ' + repr(n); print(Varible_1)
m = random.uniform(-10, 10)
Varible_2 = 'Varible_2 = ' + repr(m); print(Varible_2)
b = random.uniform(-10, 10)
Varible_3 = 'Varible_3 = ' + repr(b); print(Varible_3)

if n == m or n== b:
    print 'yes'
elif m == n or m == b:
    print 'yes'
elif b == n or b == m:
    print 'yes'
    
print(' ')

#51
print('#51')
import random

n = random.uniform(-10, 10)
Varible_1 = 'Varible_1 = ' + repr(n); print(Varible_1)
m = random.uniform(-10, 10)
Varible_2 = 'Varible_2 = ' + repr(m); print(Varible_2)
b = random.uniform(-10, 10)
Varible_3 = 'Varible_3 = ' + repr(b); print(Varible_3)

if n == m + b or m == n + b or b == n + m:
    print 'yes'

print(' ')

#52
print('#52')
import random

n = random.randint(1, 500)
Varible_1 = 'Varible_1 = ' + repr(n); print(Varible_1)
m = random.randint(1, 500)
Varible_2 = 'Varible_2 = ' + repr(m); print(Varible_2)
b = random.randint(1, 500)
Varible_3 = 'Varible_3 = ' + repr(b); print(Varible_3)
v = random.randint(1, 500)
Varible_4 = 'Varible_4 = ' + repr(v); print(Varible_4)

if n > 5 and m > 5 and b%6 == 0 and v%3 == 0:
    print 'Yez'
else: print 'No'

print(' ')

#53
print('#53')
import random

b = random.randint(1, 50)
Varible_3 = 'Varible_3 = ' + repr(b); print(Varible_3)
v = random.randint(1, 50)
Varible_4 = 'Varible_4 = ' + repr(v); print(Varible_4)

if b > 30 or v > 30:
    print 'yeZ'
    
print(' ')

#54
print('#54')
import random
t=0
for i in xrange(0, 3):
    n = random.uniform(-10, 20)
    print n
    if n < 5:
        t = t + 1
        
if t == 2:
    print 'Yez'
else: print 'No'

print(' ')

#55
print('#55')
import random
t=0
for i in xrange(0, 3):
    n = random.uniform(-10, 20)
    print n
    if n > 0:
        t = t + 1
print t

#55_1
print('#55_1')
import random

w = []
for i in range(3):
     new = random.uniform(-10, 20)
     w.append(new)
## or - w = []; w = [random.uniform(-10, 20) for i in range(3)]
## or - w = []
## w = [int(raw_input('input number: ')) 
##     for i in range(int(raw_input('input number step: ')))]

print(w)
t = 0
for i in xrange(len(w)):
    if w[i] > 0:
        t+=1
print t

print(' ')

#56
print('#56')

while 1:
    try:
        x = int(raw_input('input direction (11 < x < 14) :'))
        if x < 11: print ('Input is correct direction')
        elif x > 14: print ('Input is correct direction')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        y = int(raw_input('input command (-1, 0, 1) :'))
        if y < -1: print ('Input is correct command')
        elif y > 1: print ('Input is correct command')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')

direction = {11 : 'north', 12 : 'west', 13 : 'south', 14 : 'east'}
command = {-1 : 'left', 1 : 'right', 0 : 'forward'}

for key, value in direction.items():
    if key == x:
        a = (value)

for key, value in command.items():
    if key == y:
        b = (value)

print(a, b)

print(' ')

#57
print('#57')
while 1:
    try:
        date = int(raw_input('input date :'))
        if date < 0: print ('Input is correct date')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        month= int(raw_input('input month :'))
        if month < 0: print ('Input is correct month')
             continue
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        year = int(raw_input('input year :'))
        if year < 0: print ('Input is correct year')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')

print(date, month, year)
z = 1
if 2222 < year < 1200: z = 0
if 12 < month: z = 0
if month == 1 and 31 < date: z = 0
elif month == 2 and 28 < date: z = 0
elif month == 3 and 31 < date: z = 0
elif month == 4 and 30 < date: z = 0
elif month == 5 and 31 < date: z = 0
elif month == 6 and 30 < date: z = 0
elif month == 7 and 31 < date: z = 0
elif month == 8 and 31 < date: z = 0
elif month == 9 and 30 < date: z = 0
elif month == 10 and 31 < date: z = 0
elif month == 11 and 30 < date: z = 0
elif month == 12 and 31 < date: z = 0

if z == 1: print 'yes'

print(' ')

#57_1
print('#57_1')

def exists_year(year):
    if year > 2224 or year < 1200:
        print 'no'
    else: 
        def exists(date, month):
            month_day={1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 
                       7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        for key, value in month_day.items():
            if months <= key and day <= value: print 'yes'
            else: print 'no'
    
while 1:
    try:
        date = int(raw_input('input date :'))
        if date < 0: print ('Input is correct date')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        month= int(raw_input('input month :'))
        if month < 0: print ('Input is correct month')
             continue
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        year = int(raw_input('input year :'))
        if year < 0: print ('Input is correct year')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')

#58
print('#58')
import datetime

while 1:
    try:
        day_1 = int(raw_input('input day #1:'))
        if day_1 < 0: print ('Input is correct day')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        month_1= int(raw_input('input month #1:'))
        if month_1 < 0: print ('Input is correct month')
             continue
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        year_1 = int(raw_input('input year #1:'))
        if year_1 < 0: print ('Input is correct year')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')

while 1:
    try:
        day_2 = int(raw_input('input day #2:'))
        if day_2 < 0: print ('Input is correct day')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        month_2= int(raw_input('input month #2:'))
        if month_2 < 0: print ('Input is correct month')
             continue
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        year_2 = int(raw_input('input year #2:'))
        if year_2 < 0: print ('Input is correct year')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')

try:
    date_1 = datetime.date(year_1,month_1,day_1)
except(TypeError, ValueError):
    print ('Input is correct of first date')
        
try:
    date_2 = datetime.date(year_2,month_2,day_2)
except(TypeError, ValueError):
    print ('Input is correct of second date')
        
if year_1 < year_2 : z = 1
else: z = 0

if z != 0 and month_1 < month_2 : x = 1
else: x = 0

if day_1 < day_2 : c = 1
else: c = 0

if z == 1 : print 'yes'
elif z == 0 and x == 1 : print 'yes'
elif z == 0 and x == 0 and c == 1 : print 'yes'
else: print 'no'

print(' ')

#59
print('#59')

while 1:
    try:
        y = int(raw_input('input number :'))
        if 9999 < y < 1000:
            print ('Input is correct the four-digit number')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')

a = y/1000; b = y/100 - a*10; c = y/10 - 100*a - 10*b
d = y - 1000*a - 100*b - 10*c

if a > b and b > c and c > d:
    print 'yes'
else: print 'no'

print(' ')

#60
print('#60')
while 1:
    try:
        y = int(raw_input('input number :'))
        if 999 < y < 100:
            print ('Input is correct the four-digit number')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')

set = 'input number: ' + repr(y); print (set)
a = y/100; b = y/10 - a*10; c = y - 100*a - 10*b
y = c*100 + b*10 + a
set = 'output number: ' + repr(y); print (set)

print(' ')

#61
print('#61')

while 1:
    try:
        u = int(raw_input('input number :'))
        if 9999 < u < 1000:
            print ('Input is correct the four-digit number')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')

a = u/1000; b = u/100 - a*10; c = u/10 - 100*a - 10*b
d = u - 1000*a - 100*b - 10*c

if a == b or a == c or a == d: print 'yes'
elif b == a or b == c or b == d: print 'yes'
elif c == a or c == b or c == d: print 'yes'
elif d == a or d == b or d == c: print 'yes'
else: print 'no'

print(' ')

#62
print('#62')


while 1:
    try:
        u = int(raw_input('input number :'))
        if 99999 < u < 10000:
            print ('Input is correct the five-digit number')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
a = u/10000; b = u/1000 - a*10; c = u/100 - 100*a - 10*b
d = u/10 - 1000*a - 100*b - 10*c
e = u - 10000*a - 1000*b - 100*c - 10*d

u = 10000*a + 100*c + e

print (' ')

#63
print ('#63')
while 1:
    try:
        y = int(raw_input('input number 1 :'))
        if 999 < y < 100:
            print ('Input is correct the four-digit number')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        t = int(raw_input('input number 2 :'))
        if 999 < t < 100:
            print ('Input is correct the four-digit number')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
set = 'Here is input number 1: ' + repr(y); print (set)
a1 = y/100; b1 = y/10 - a1*10; c1 = y - 100*a1 - 10*b1
y = c1*100 + b1*10 + a1


set = 'Here is input number 2 : ' + repr(t); print (set)
a2 = t/100; b2 = t/10 - a2*10; c2 = t - 100*a2 - 10*b2
t = c2*100 + b2*10 + a2

r = a1*100000 + b1*10000 + c1*1000 + a2*100 + b2*10 + c2
set = 'Result a six-digits number : ' + repr(r); print (set)

print (' ')

#64
print('#64')

while 1:
    try:
        u = int(raw_input('input number :'))
        if 9999 < u < 1000:
            print ('Input is correct the four-digit number')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')

a = u/1000; b = u/100 - a*10; c = u/10 - 100*a - 10*b
d = u - 1000*a - 100*b - 10*c

if (a*10 + b) == (d*10 + c): print 'yes'
else: print 'no'

print (' ')

#65
print ('#65')

while 1:
    try:
        u = int(raw_input('input number :'))
        if 9999 < u < 1000:
            print ('Input is correct the four-digit number')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')

a = u/1000; b = u/100 - a*10; c = u/10 - 100*a - 10*b
d = u - 1000*a - 100*b - 10*c

if a < 5: u = a*1000 + b*100 + c*10 + d
elif b < 5: u = b*1000 + a*100 + c*10 + d
elif c < 5: u = c*1000 + a*100 + b*10 + d
elif d < 5: u = d*1000 + a*100 + b*10 + c
else: print 'no'

set = 'Result number : ' + repr(u); print (set)

def polinom(u):
    a = []; t = 0
    # определить число разрядов в введённом числе
    k = len(str(u))
    # вычисление каждой цифры числа, начиная со старшего разряда
    # цикл работает со старшего значения -- на убывание, а не как обычно
    # на возрастание. За счёт применения параметра reversed
    for n in reversed(xrange(k)):
        a[n] = u/(10^(n)) - t
        for i in reversed(xrange(k)):
            t = (a[n])*(10^(n-i))
            a[n] = a[n] + t
            
        

            
        
#68
print('#68')
# Чтобы работать с комплексными значениями от извлекаемого 
# корня дискриминанта (неохота заморачиваться с проверками на значение
# дискриминанта и писать что корней нет), импортирую математическию
# библиотеку для работы с комплексными числами 
import cmath

while 1:
    try:
        a = int(raw_input('input number  "a" :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        b = int(raw_input('input number  "b" :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        c = int(raw_input('input number  "c" :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
x1 = ((-b) + cmath.sqrt((b^2) - 4*a*c))/(2*a)
root_1 = 'x1 = ' + repr(x1); print (root_1)

x2 = ((-b) - cmath.sqrt((b^2) - 4*a*c))/(2*a)
root_2 = 'x2 = ' + repr(x2); print (root_2)

print(' ')

#69
print('#69')
import math

while 1:
    try:
        a = int(raw_input('input number  "a" :'))
        if a <= 0:
            print ('Input is correct the side of size "a" ')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        b = int(raw_input('input number  "b" :'))
        if b <= 0:
            print ('Input is correct the side of size "b" ')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        c = int(raw_input('input number  "c" :'))
        if c <= 0:
            print ('Input is correct the side of size "c" ')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
p = (a + b + c)/2

try:
    S = math.sqrt(p*(p - a)*(p - b)*(p - c))
except(TypeError, ValueError):
    print ("The triangle doesn't exist")
    S = 0

if  S > 0:
    S = 'The triangle square = ' + repr(S); print S

print(' ')

#70
print('#70')

while 1:
    try:
        a_x = int(raw_input('input a coord X point "a" :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        a_y = int(raw_input('input a coord Y point "a" :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        b = int(raw_input('input a coord X point "b" :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        b = int(raw_input('input a coord X point "b" :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        c = int(raw_input('input a coord X point "c" :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')

while 1:
    try:
        c = int(raw_input('input a coord Y point "c" :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
if x_a != x_b and y_a != y_c:
    print 'Input correct coords of points'
else:
    x_d = x_c; y_d = y_a
    coords_d = 'Coords is point d :' + repr([x_d, y_d])
    print coords_d
print (' ')

#71
print('#71')

while 1:
    try:
        h = int(raw_input('input number hour :'))
        if h <= 0:
            print ('Input is correct of hour')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        m = int(raw_input('input number minute :'))
        if m <= 0:
            print ('Input is correct of minutue')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')

# Приведение введённого времени к корректному значению
while 1:
    if 60/m == 0:
        m = m - 60
        continue
    break
    
while 1:
    if 12/h == 0:
        h = h - 12
        continue
    break
    
# Вычисление угла
angle = (abs(float((h + m/60.)*30. - m*6.)))
angle = 'Angle between arrows = ' + repr(angle); print angle
print(' ')

#72
print('#72')

while 1:
    try:
        a_x = int(raw_input('input a coord X point "a" :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        b_x = int(raw_input('input a coord X point "b" :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        h_a = int(raw_input('input a size side "a" first rectangle :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        l_a = int(raw_input('input a size side "b" first rectangle :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        h_b = int(raw_input('input a size side "a" second rectangle :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')

while 1:
    try:
        l_b = int(raw_input('input a size side "b" second rectangle :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        




#73
print('#73')

while 1:
    try:
        a_x = int(raw_input('input a coord X point "a" :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        b_x = int(raw_input('input a coord X point "b" :'))
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        h_a = int(raw_input('input a height side "a" first rectangle :'))
        if h_a <= 0:
            print ('Input is correct of height side "a"')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        l_a = int(raw_input('input a length side "a" first rectangle :'))
        if h_a <= 0:
            print ('Input is correct of length side "a"')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
while 1:
    try:
        h_b = int(raw_input('input a height side "a" second rectangle :'))
        if h_a <= 0:
            print ('Input is correct of height side "b"')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')

while 1:
    try:
        l_b = int(raw_input('input a length side "b" second rectangle :'))
        if h_a <= 0:
            print ('Input is correct of length side "b"')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
# Определить, принадлежат ли все точки первого прямоугольника второму
if x_a >= x_b and y_a >= y_b \
and l_a - l_b <= 0 and h_a - h_b <= 0:
    print 'All point rectangle A belong rectangle B'
else: print 'All point rectangle A Don`t belong rectangle B'
    
# Определить, принадлежат ли все точки одного из прямоугольников другому
if x_a <= x_b and y_a <= y_b \
and l_a - l_b >= 0 and h_a - h_b >= 0:
    print 'All point rectangle B belong rectangle A'
else: print 'All point rectangle B Don`t belong rectangle A'

# Определить, пересекаются ли эти прямоугольники
if x_a >= x_b + l_b or x_a + l_a >= x_b and \
y_a >= y_b + h_b or y_a + h_a >= y_b:
    print 'Rectangles aren`t crossed'
else: print 'Rectangles are crossed'

print (' ')

#74
print('#74')
## Бредовое какое-то задание
while 1:
    try:
        number = int(raw_input('input integer number from 1 to 180 :'))
        if 180 < number < 1:
            print ('Input is correct of number')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
for u in xrange(number):
    digit = 10 + u
    
print(digit)


#75
print('#75')

for you in xrange(10):
    print'"You are welcome!"'
print(' ')

#76
print('#76')

while 1:
    try:
        number = int(raw_input('input integer number :'))
        if number <=0:
            print ('Input is correct of number')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')

for i in xrange(number):
    print '"Silence is golden"'

print(' ')    

#77
print('#77')

while 1:
    try:
        number = int(raw_input('input integer number :'))
        if number <=0:
            print ('Input is correct of number')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')

for i in xrange(number):
    print '00000'
    
print(' ')

#78
print('#78')


while 1:
    try:
        size = int(raw_input('input size :'))
        if size <=0:
            print ('Input is correct of number')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')

string = '*'
length = string * size
for i in xrange(size):
    print length
    
print(' ')

#79
print('#79')

for i in xrange(1, 21):
    print i
print(' ')

#80
print('#80')

for i in xrange(1001, 1026):
    print i
print(' ')

#81
print('#81')

for n in reversed(xrange(101)):
    if n >= 0:
        print n
    else: break
print(' ')

#82
print('#82')

t = 1.2

while 1:
    print t
    t = t + 0.2
    if t > 3:
        break
print(' ')

#83
print('#83')

a = '25  25.5  24.8'
b = '26 26.5 25.8'
c = '35 35.5 34.8'
print a; print b; print c
print(' ')

#84
print('#84')

while 1:
    try:
        size = int(raw_input('input rate buks :'))
        if size <=0:
            print ('Input is correct of number')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')

for i in xrange(1, 101):
    print i, '$ --', size*i, 'Rub --', i*0.18,'kg'
   
print(' ')

#85
print('#85')
while 1:
    try:
        string = int(raw_input('input number :'))
        if string <=0:
            print ('Input is correct of number')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')
        


#86
print('#86')
while 1:
    try:
        string = int(raw_input('input number N :'))
        if N <=0:
            print ('Input is correct of number')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')

t = 0        
for i in xrange(1, N + 1):
    t = t + i

print t

print(' ')

#87
print('#87')

t = 10        
for i in xrange(1, 79):
    t = t + i

print t

print(' ')

#88
print('#88')

t = 5        
for i in xrange(6, 14):
    t = t * i

print t

print(' ')

#89
print ('#89')

t = 1; c = 1
while t < 112:
	t = t + 3
	c = c + t
	
print c

print(' ')

#90
print ('#90')
import math

z = 1.; cos = 0.
while z < 111:
	z = z + 2.
	cos = cos + math.cos(z/(z+2.))
	
cosin = 'Sum cos = ' + repr(cos); print cosin

print(' ')

#91
print('#91')

m = 1.; d = 0.
while m < 9:
	m = m + 1.
	print m
	d = d + m/(m + 1.)
	
diff = 'Diff =' + repr(d); print diff

print(' ')	

#92
print('#92')
# Задания не понял, хотя на вид ничего сложного

#93
print('#93')

while 1:
    try:
        string = int(raw_input('input number n :'))
        if n <=0:
            print ('Input is correct of number')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')

k = 1; sq = 0
while k < n:
	k = k + 1
	sq = sq + k*k
	
sum_sq = 'Sum squere = ' + repr(sq +1); print sum_sq

print(' ')

#94
print('#94')

while 1:
    try:
        string = int(raw_input('input number n :'))
        if n <=0:
            print ('Input is correct of number')
            continue
        break
    except(TypeError, ValueError):
        print ('Input is number')
        
t = 1.; g = 0.
while t < n:
	t = t + 1.
	g = g + 1./t
	
ga = 'G serial = ' + repr(1. + g); print ga

print(' ')

#95
print('#95')
import random

a = random.randint(1, 50)
Varible_a = 'Varible_a = ' + repr(a); print(Varible_a)
n = random.randint(1, 50)
Varible_n = 'Varible_n = ' + repr(n); print(Varible_n)

p = 1; l = 0
for i in xrange(1, n + 1):
	l = (a + i)*(a + i)
	p = p*l

p = 'p = ((a+1)^2)*((a+2)^2)*...*((a+n)^2) = ' + repr(p)
print p

print(' ')

#96
print('#96')

import math
import random

x = random.randint(0, 360)
Varible_x = 'Varible_x = ' + repr(x); print(Varible_x)
n = random.randint(1, 30)
Varible_n = 'Varible_n = ' + repr(n); print(Varible_n)
	

dcos = 0.; summ = 0.
for i in xrange(1, n + 1):
	dcos = 1./(math.cos(math.pow(x,i)))
	summ = summ + dcos
	
summ = 'Summa = ' + repr(summ); print summ 

print (' ')

#97
print ('#97')

import random

n = random.randint(1, 150)
Varible_n = 'Varible_n = ' + repr(n); print(Varible_n)

t = 1; prod = 1; summa = 0
for i in xrange(1, n + 1):
	t = i*(i + 1)
	print i
	print t
	
#98
print('#98')

import random

# Описание увеличения пробега лыжника на 10% каждый день.
def lyzhnik(day):
	l = 10.
	for i in xrange(1, day):
		l = l*1.1
	return l

# Пробег лыжника на второй, третий, ..., десятый деньтренировки		
for u in xrange(2, 10):
	print lyzhnik(u)

# суммарный путь за неделю тренировок
t = 0		
for s in xrange(1, 8):
	print s
	t = t + lyzhnik(s)
	
week = 'Week  mileage = ' + repr(t); print week

# суммарный путь за n-дней
n = random.randint(2, 50)
d = 0
for s in xrange(1, n + 1):
	d = d + lyzhnik(s)

n_days = 'n-days milege = ' + repr(d); print n_days

# На какой день он одолеет 80 км за тренировку
days = 1
while l <= 80:
	l = lyzhnik(days)
	days = days + 1
	
days = 'Days 80 km milege = ' +repr(days); print days

print (' ')

#99 
print ('#99')

i = 1000
while i < 9999:
	a = i/1000; b = i/100 - a*10; c = i/10 - 100*a - 10*b
	d = i - 1000*a - 100*b - 10*c
	if a != b and a != c and a != d and b != c and b != d and c != d:
		print i
	i+=1
print(' ')

#100
print ('#100')

i = 1000
while i < 9999:
	a = i/1000; b = i/100 - a*10; c = i/10 - 100*a - 10*b
	d = i - 1000*a - 100*b - 10*c
	if  a != 5 and a != 6 and b != 5 and b != 6 \
	and c != 5 and c != 6 and d != 5 and d != 6:
		print i
	i+=1
print(' ')

#101
print('#101')

i = 10000
while i < 99999:
	a = i/10000; b = i/1000 - a*10; c = i/100 - 100*a - 10*b
	d = i/10 - 1000*a - 100*b - 10*c
	e = i - 10000*a - 1000*b - 100*c - 10*d
	if e%2 == 0 and c%2 != 0 and (a+b+c+d+e)%4 == 0:
		print i
	i+=1
print(' ')

#102
print('#102')

i = 1000
while i < 9999:
	a = i//1000; b = i//100 - a*10; c = i//10 - 100*a - 10*b
	d = i - 1000*a - 100*b - 10*c
	if a == 3 or b == 3 or c == 3 or d == 3: print i
	i+=1
print(' ')

#103
print('#103')

j = 100
while j < 999:
	a = j//100; b = j//10 - a*10; c = j - 100*a - 10*b
	if j == a**3 + b**3 + c**3: print j
	j+=1
print(' ')

#104
print('#104')

j = 1000; z = 0
while j < 9999:
	a = j//1000; b = j//100 - a*10; c = j//10 - 100*a - 10*b
	d = j - 1000*a - 100*b - 10*c
	if 600*j > (a + b + c + d): z+=1
	j+=1
	
print z

print(' ')

#105
print('#105')

n = 11
while n < 9999:
	if n%11 == 0 and n%2 == 1 and n%3 == 1 and n%4 ==1 and n%5 == 1 \
	and n%6 == 1 and n%7 == 1 and n%8 == 1 and n%9 == 1 and n%10 == 1:
		print n
	n+=1
print('????')

#106
print('#106')

import random
n = random.randint(2, 10)

print n*'1'; print 2*n*'2'; print 3*n*'3'

print('')

#107
print('#107')

for n in reversed(xrange(11)):
	
	print n





t = [10, 9, 10, 10, 9, 8]

for i in t:
	if (t.count(i)==1):
		t.remove(i)
		

# Пароль как строка (str, unicode).
try:
	if 10 <= len(password) <= 64 and \
	password.isalnum() == 1 and \
	password.islower() == 1 and \
	password.isupper() == 1:
		print ('True')
    else: print ('False')
except(TypeError, ValueError):
	print ('False')

re.match("[a-zA-Z0-9]+", password)

