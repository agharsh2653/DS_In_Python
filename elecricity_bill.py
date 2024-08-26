unit  = int(input("Enter the unit "))
amount = 0
if(unit <= 50):
     amount = unit*0.5
elif(unit >50 and  unit<=150):
     amount = 25+ (unit-50)*0.75
elif(unit >150 and  unit<=250):
     amount = 25+75+ (unit-150)*1.2
else:
     amount = 25+75+120+ (150-50-unit)*1.5

bill = amount+ amount*0.2
print(f"Your electricity will be {bill}")

