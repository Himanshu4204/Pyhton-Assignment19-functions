#Write a python program to sum all the numbers in a list.?
def add():
    s=input("Enter Numbers seperated with commas :")
    l=[ int(e) for e in s.split(',')]
    return sum(l)
x=add()
print("Sum of  All Numbers is :",x)