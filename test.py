print('Hello world')
###

xx = 65 #int
xz = 65.9 #float
xy = 'Hello world'
x = ['Donald', ' ', 'Edwin'] #list

print (x, xy, xx, xz)
print (type(xy))
print (type(xx))
print (type(xz))

###
age = 40
if age > 10:
    print ('Pay for ticket')
else:
    print ('Travel for free')

###
if age > 20:
    print ('Pay for ticket')
elif age > 100:
    print ('You are already dead')
else:
    print ('Travel with Cytravel for free')

###
isMember = True
if age >= 30:
    if isMember:
        print ('welcome to the club')
    else:
        print ('sign in as member')
else: 
    print ('you are still young')

S = 'Adult' if age > 18 else 'Minor '
print (S)

###
n = 4
for i in range(0, n):
    print (i)

###
number = 5
while number < 10:
    number = number + 1
    print (number)

###
b = "DoanldEdwin"
print(b[:6])

a = "2"
b = "3"

print (a + b)

name = input('Enter you name: ')
print ('Hello ' + name)