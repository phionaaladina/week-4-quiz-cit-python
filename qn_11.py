#Write a function to compute 5/0 and use try/except to catch the exceptions.

def division():
   return 5/0
try:
   division()
except ZeroDivisionError:
       print ("Division by zero is not possible!!!")
except Exception as  error:
        print ('Caught an exception:',error)
finally:
       print ('Nice try.')