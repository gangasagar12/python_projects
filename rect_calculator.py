# input  we need from the user
# total rent
# total food ordered for snacking
#electricity units spend
#  total number of people staying in house
#charge per unit
 
 # total amount you have pay in a month

rent=int(input("enter total rent amount :"))
food=int(input("enter total food amount: "))
electricity_unit=int(input("enter total electricity spend on whole months: "))
charger_unit=int(input("enter charge per unit: "))
people=int(input("enter total number of people staying in house: "))

total_bills=electricity_unit*charger_unit
output=(rent+food+total_bills)/people

print("each person has to pay : ",output)