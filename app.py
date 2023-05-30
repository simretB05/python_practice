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


