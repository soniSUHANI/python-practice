sub1= int(input("Enter marks in sub 1: "))
sub2 = int(input("Enter marks in sub2: "))
sub3= int(input("Enter marks in sub3: "))
sum = sub1 +sub2+sub3
if (sub1<33 or sub2<33 or sub3<33):
    print("You are failed")
elif sum /3< 40:
    print("you are fail due to total percentage less than 40")
else:
    print("congratulations! You are passed")

