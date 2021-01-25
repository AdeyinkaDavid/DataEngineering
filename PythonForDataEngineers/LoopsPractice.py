def colors():
    usrColor = input(str("What is your favorite color? "))
    if usrColor == 'Red' or 'red' or 'RED':
           print("I love {} too".format(usrColor))
    else:
        print("I do not like {} too".format(usrColor))


colors()



