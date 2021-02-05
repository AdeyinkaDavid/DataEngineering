# def colors():
#     usrColor = input(str("What is your favorite color? "))
#     if usrColor == 'Red' or 'red' or 'RED':
#            print("I love {} too".format(usrColor))
#     else:
#         print("I do not like {} too".format(usrColor))


# colors()

# def example4(*args, color = 'red', **kwargs):
#     print(args)
#     print(kwargs)
#     print(colors)

#     for i in args:
#         print(i)
#         if i == 'red':
#             return f"done!"
#             print("I am here")
#         else:
#             return f"I do not like {i}"

# example4()



##Write a function that can accept a list and array as an argument and return a
#  unique value of the argument passed

x = [1, 5, 5, 3, 2 ,5, 7, 8]

def unique(x):
    #Set does not take duplicate, so by converting the list into a set, it automatically eliminates it, and only prints the unique value
    #setList = set(x)
    #return setList
    uniqueList = []

    for y in x:
        if y not in uniqueList:
            uniqueList.append(y)

    #Loop through the unique list and print the list
    for y in uniqueList:
        print(y)

        
    
print(unique(x))
