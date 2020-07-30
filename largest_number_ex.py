#Finding the largest Value
largest_so_far=-1
print('Before', largest_so_far)
for the_num in [9,41,12,3,74,15]:
    if the_num>largest_so_far:
        largest_so_far=the_num
    print(largest_so_far, the_num)
print('After', largest_so_far)

#OUTPUT = Before -1 / 9 9 / 41 41 / 41 12 / 41 3 / 74 74 / 74 15 / After 74
# Another example

smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)
