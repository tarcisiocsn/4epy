#to count how many times we execute loop, we introduce a counter variable that starts at 0
#and we add one to it each time through the loop
print('Counting a loop')
zork=0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork=zork+1 # inicio da contagem de numeros do loop
    print(zork, thing)
print('After', zork)

#output
#1 9
#2 41
#3 12
#4 3
#5 74
#6 15
#after 6

#Summing in a loop
print('Summing in a loop')
zork=0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork=zork+thing
    print(zork, thing)
print('After', zork)

#Finding the Average in a loop
# I gonna change the variables name
print('Average in a loop')
count=0
sum=0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count=count+1
    sum=sum+value
    print(count, sum, value)
print('After', count, sum, sum/count) # the last one is the average

#Filtering in a loops
print('Filtering in a loop')
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if value>20:
        print('Large Number', value)
print('After')

#Search Using a Boolean Variable
#it has only two values - true or false
#If we just want to search and know if a value was found, we use a variable that starts at False and is set to True  as soon as we find what we are looking for
print('python search 01')
found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found=True
    print(found, value)
print('After', value)

#Finding the largest Value
print('Finding the largest value')
largest_so_far=-1
print('Before', largest_so_far)
for the_num in [9,41,12,3,74,15]:
    if the_num>largest_so_far:
        largest_so_far=the_num
    print(largest_so_far, the_num)
print('After', largest_so_far)

#Finding the smallest value
print('Finding the smallest value')
smallest=None
print('Before')
for value in [9,41,12,3,74,15]:
    if smallest is None:
        smallest=value
    elif value < smallest:
        smallest=value
    print(smallest, value)
print('After', smallest)

#The is and is not operators
# python has  an 'is' operator that can be used in logical expressions
#implies 'is the same as'
#similar as ==, but stronger
# is not also is a logical operator
#0==0.0 true
#0 is 0.0 false because 'is' is stronger than ==
#don't use 'is' on float, str
#use on none and booleans (true false)
