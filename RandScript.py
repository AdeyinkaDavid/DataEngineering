#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import random 

"""
This program will generate random numbers between 2 numbers
"""
def my_function():
    QuestionToUser = str(input("Do you want to play a game of random numbers? \nEnter yes or no: "))

    
    if QuestionToUser != 'yes':
        print('Bye bye')
    else:
        while QuestionToUser == 'yes':
           num1 = 5 #int(input('Enter any number: ')) 
           num2 = 20 #int(input('Enter another number: '))
            
           print("Rolling the dices, Please wait!")
           print('Rolling dice 1: ',random.randint(num1,num2))
           print('Rolling dice 2: ',random.randint(num1,num2))
           print('Rolling dice 3: ',random.randint(num1,num2))
                
           QuestionToUser = str(input('Do you want to keep rolling? '))
           
           if QuestionToUser != 'yes':
               print('bye bye')
                
print(my_function())

'''
Create a cron JOB that runs this python script every hour, and then there should be a 
different result for each time it runs. Each result will be in a different file that 
will be named result(datetime).txt and it will save it in our target folder 

HINT: We can concatenate the file names to include the date time when we do 
run script >> result + 'getdate()' -> So each time we run our script it will create 
a new file and then attach the current time it ran the script.

'''     
        
            
            
    


