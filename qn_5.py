'''
Write a python program to fetch only Email ID from text file which include following fields -:
Name
Mobile Number
Roll Number
Email ID
'''
import re
print('Email ID')

file = open("file.txt")
for line in file:
    line = line.strip()
    emailID = re.findall("[0-9a-zA-z]+@[0-9a-zA-z]+\.[0-9a-zA-z]+", line)
        
    if(len(emailID) > 0):
        print(emailID)
 
