list1 = [1,2,3,4,5,6,7,8]
list2 = [1,2,3,4,5,6,7,8,9,10,11,12]

#test for prime numbers numbers need to only divide by themselves and 1
prime = []
notprime = []
for i in list1[::-1]: 
    temp = i 
    for i in list1:
        if temp & i == 0:
            if i == temp or i == 1:
                prime.append(temp)
print(prime)
#print(notprime)