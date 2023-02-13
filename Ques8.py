#Write a program to multiply all the numbers in a list?
def multi():
    s=input("Enter Numbers you want to Multiply seprated by spaces :")
    l=[ int(e) for e in s.split()]
    multiply=1
    for num in l:
        multiply *=num
    return multiply
x=multi()
print("Multiply of all numbers is :",x)





