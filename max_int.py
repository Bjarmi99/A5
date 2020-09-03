num_int = int(input("Input a number: "))    # Do not change this line

# while user enters positive integer numbers
# we find the highest integer enterd
# if a negative integer is enterd then we stop and print the max_int
max_int=0
while num_int>=0:
    max_int=max(max_int,num_int)
    num_int = int(input("Input a number: "))

print("The maximum is", max_int)    # Do not change this line
