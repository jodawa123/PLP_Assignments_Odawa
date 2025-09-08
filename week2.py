my_list=[]
new=[10,20,30,40]
for i in new:
    my_list.append(i)
    
my_list.insert(1,15)  
another=[50,60,70]
my_list.extend(another)
my_list.pop(-1)
my_list.sort

if 30 in my_list:
    print( "The index of 30 is:",my_list.index(30))
    
    
    
print(my_list)