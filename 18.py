

a = int(input("Enter Your Eng Mks :"))
b = int(input("Enter Your Math Mks :"))
c = int(input("Enter Your Hindi Mks :"))
d = int(input("Enter Your Science Mks :"))

avg=a+b+c+d

# total=avg

percent = ( avg/4)

print("Your Total mks is : ",avg)
print("Your Percentage Is :" , percent)

if percent < 40 :
      print("Your Failed")
elif 90 < percent :
      print("Your In Topper List ")
else:
      print("Your Passed")

