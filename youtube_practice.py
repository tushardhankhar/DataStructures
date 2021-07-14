expense=[2200,2350,2600,2130,2190]
flag=0

d=expense[1]-expense[0]
total_first_qtr = expense[0]+expense[1]+expense[2]

for i in range(0,len(expense)):
    if(expense[i]==2200):
        flag=1
if(flag==1):
    print("true")
else:
    print("false")

print(2190 in expense) #something new , to search something in a list

print(d)
print(total_first_qtr)

expense.append(1980)
print(expense)

a=expense[3]-200
expense[3]=a
print(expense)

