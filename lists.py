
a=[]

for i in range(5):
    number= int(input("Enter your  numbers: "))
    a.append(number)  

print("Numbers entered are:" ,a)

sum=0
for i in a:
   sum+=i

print ("The sum of these numbers is: ", sum)



