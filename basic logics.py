#1 average of 3 numbers

n1=int(input("Enter num 1"))
n2=int(input("Enter num2"))
n3=int(input("Enter num3"))
sum=n1+n2+n3
avg=sum/3
print("Average of",n1,n2,"and",n3,":",avg)

#2. Find the profit percentage by using selling price and cost price

sp=600
cp=500
profit=sp-cp
print("profit = ",profit)
profit_percentage=(profit/cp)*100
print(profit_percentage, "%")

#3.find the missing angle in triangle by taking 2 angles.
a1=50
a2=60
sum=a1+a2
missing_angle=180-sum
print("missing_angle",missing_angle)

#4.find the last digit of given number
num=15
last_digit=n%10
print("last digit of number is",last_digit)

#5.remove last digit from given number
num=156
rm=num//10
print(rm)


#find the first digit of 4 digit number
num=int(input("Enter a 4-digit number :"))
first_digit=num//1000
print("First digit of 4-digit number is :",first_digit)


#find sum of first n natural numbers
num=int(input("Enter a number :"))
sum=num*(num+1)//2
print("sum of first",num,"natural numbers :",sum)

#find the average of first n natural numbers
num=int(input("Enter a number :"))
avg=(num+1)/2
print("Average of first",num,"natural numbers :",avg)

#find the gross salary 
basic_salary=20000
b="20%"
i="5%"
bonus=(20/100)*20000
incentives=(5/100)*20000
gross_salary=(basic_salary+bonus+incentives)
print(gross_salary)

#find inhand salary
basic_salary=20000
bonus_per="20%"
incentives_per="5%"
pf_per="2%"
health_insurance_per="1%"
bonus=(20/100)*20000
incentives=(5/100)*20000
pf=(2/100)*20000
health_insurance=(1/100)*20000
gross_salary=(basic_salary+bonus+incentives)
deductions=pf+health_insurance
inhand_salary=gross_salary-deductions
print("inhand_salary:",inhand_salary)

#swap 2 numbers
a=10
b=20
print("Before Swapping")
print("a = ",a)
print("b = ",b)
c=a
a=b
b=c
print("After Swapping")
print("a = ",a)
print("b = ",b)
#using 2 variables
a=10
b=20
print("Before Swapping")
print("a = ",a)
print("b = ",b)
a=a+b
b=a-b
a=a-b
print("After Swapping")
print("a = ",a)
print("b = ",b)

a=10
b=20
print("Before Swapping")
print("a = ",a)
print("b = ",b)
a=a*b
b=a//b
a=a//b
print("After Swapping")
print("a = ",a)
print("b = ",b)