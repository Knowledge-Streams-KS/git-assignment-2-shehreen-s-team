import sqRoot
from multiply import multiplyNumbers
from division import divideNumbers
import mod;

def main():
    value1 = input("enter first value\n")
    value2 = input("enter second value\n")
    squareRoot = sqRoot(value1)
    print("squareroot of ", value1," is ", squareRoot )
    print(value1, " mod ", value2, "is: ", )
    multiplyNumbers(value1, value2)  
     divideNumbers(value1, value2)

main()