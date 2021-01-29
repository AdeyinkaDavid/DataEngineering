#a = 4

#def counter():
 #   global a 
#    for i in range(a):
 ##       print(i) 

#counter()

#def counter2(start= 1, b):
 #   for i in range(start, end):
#        print(i, end=" ")

#counter2(7)


########## BUBBLE SORT
z = [10, 7, 5, 3, 1 , 0.5]

def MyFunc(a):
    lengt = len(a)
    for i in range(lengt):
        for m in range(0, lengt-i-1):
            if a[m] > a[m+1]:
                print(a[m+1], a[m])
                a[m], a[m+1] = a[m+1], a[m]
    return a
for i in range(len(z)):
    print(z[i])

print(MyFunc(z))


#for i in range(len(a)): 
#    for m in  range(0, len(a)-1):  --> Ensure we have a number that starts with 0 so we can pick up the first index, and the last index of my array 
#if a[m] > a[m+1]:
    #a[m], a[m+1] = a[m+1], a[m] 


        # a[m] > a[m + 1] 