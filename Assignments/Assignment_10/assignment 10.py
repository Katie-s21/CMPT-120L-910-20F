import argparse
import logging
import sys
log = open('assignment10.log', 'a')
sys.stdout = log

logging.basicConfig(filename='assignment10.log',level=logging.DEBUG)

parser = argparse.ArgumentParser()

parser.add_argument('--integer', action='store', dest='integer', type=int, help='this is the number we will find the sigma notation of')

args = parser.parse_args()

logging.info("Please enter desired number")

args = input()

print(args)

logging.info('This is your desired number.')

if int(args) >= 0:
    arr = []
for i in range(int(args)):
    arr.append(i)
x = (sum(arr))
y = int(args)
result = x + y
print(result)
logging.info('This is the sigma notation of your desired number.')

       
#I wasn't able to make this into a function. I couldn't get the variables to pass through. Not sure why. I have tried for hours.


       


   
      
    


        






