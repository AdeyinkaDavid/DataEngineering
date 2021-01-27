def colors():
    usrColor = input(str("What is your favorite color? "))
    if usrColor == 'Red' or 'red' or 'RED':
           print("I love {} too".format(usrColor))
    else:
        print("I do not like {} too".format(usrColor))


colors()

def example4(*args, color = 'red', **kwargs):
    print(args)
    print(kwargs)
    print(colors)

    for i in args:
        print(i)
        if i == 'red':
            return f"done!"
            print("I am here")
        else:
            return f"I do not like {i}"

example4()
