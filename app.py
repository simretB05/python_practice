# Write a function that takes 1 number as an arugment and returns that number squared
def squareNumbers(num):
   return num*num

sqNumber=squareNumbers(8)
print(sqNumber)
# Write a function that takes 3 numbers as arugments as returns the largest one.
def largeNumber(num_one,num_two,num_three):
   if(num_one>num_two and num_one >num_three):
    return  num_one
   elif(num_two>num_one and num_two>num_three):
     return num_two
   else:
     return num_three
   
largeNum= largeNumber(100,700,900)
print(largeNum)
# Write a function that takes 1 number and will return True if the
# number is even and False otherwise
def check_if_even(num):
  if(num%2==0):
   return True
  else:
    return False
  
checkIfeven=check_if_even(41)
print(checkIfeven)
#  Write a function that takes 1 array of numbers as an arugment and will
# print out each one
def printNumbers(numbers):
    for num in numbers:
     print(num)
  
arry_of_nums=(1,2,3,4,5)
numPrint=printNumbers(arry_of_nums)
# Write a function that takes 1 array of numbers returns the sum of all
# numbers in the array
def SumNumbers(numbers):
    total=0
    while(total<len(numbers)):
        for num in numbers:
         total= num+total
        return total
    
arry_of_nums=(1,2,3,4,5,9,30)
numSum=SumNumbers(arry_of_nums) 
print(numSum) 

# Write a function that takes 1 array of numbers and returns the sum of
# all numbers in the array that are even numbers

def sum_if_even(numbers):
    total=0
    while(total<len(numbers)):
        for num in numbers:
         if(num%2==0):
           total= num+total
        return total
arry_of_numsEven=(1,2,3,4,5,9,12,16,20,24,30,)
numSumEven=sum_if_even(arry_of_numsEven) 
print(numSumEven) 
  