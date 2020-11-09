from colorama import Fore
import os
import time
import sys

os.system('cls' or 'clear')
import sys
from colorama import init, AnsiToWin32, Fore, Back
# init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream
# print(Fore.GREEN, "This is green text", file=stream)
print(" ")
print(Fore.GREEN,"welcome to my tool",file=stream)
print(" ")
print(Fore.RED,"please enter num1",file=stream)
num1 = input(" >>>")
try:
    num1 = int(num1)
except :
    print(" ")
    print("syntax error")
    time.sleep(2)
    exit()
    pass
print(" ")
print(Fore.RED,"please enter num2",file=stream)
num2 = input(" >>>")
try:
    num2 = int(num2)
except :
    print("syntax error")
    time.sleep(2)
    exit()
    pass


sum1 = num1 +num2
sum1=str(sum1)
print(Fore.BLUE,"sum:"+ sum1 , file=stream)
