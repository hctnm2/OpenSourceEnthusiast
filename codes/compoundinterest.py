# Python code
# To find compound interest

# inputs
p= 1200 # principle amount
t= 2	 # time
r= 5.4 # rate
# calculates the compound interest
a=p*(1+(r/100))**t # formula for calculating amount
ci=a-p # compound interest = amount - principal amount
# printing compound interest value
print(ci)
