# i am taking a list 
a = [1 , 3 , 5 , 6 , 6  , 7,8 ,10]
# now I am applying ****append method*****
a.append(50) # add element at the last of the list 
print(a)

#Insert(index,value)
s = [30 , 60 , 40 , 100 , 70]
s.insert(3,"Sourav bali")
print(s)

#extend(list that you want to attach)
list1 = ['s','x','zw']
s.extend(["s","t"])
print(s)

# Remove (element value) ismai jo hum method ke andar value dete hai wo remove ho jati hai 
number = [10, 50 , 79 , 100 , 699]
number.remove(100)
print(number)


# pop() method mai agar koi hum value nhi dete toh last ka element delete hoga
numbers = [100,90,4000, 5000]
numbers.pop()
print(numbers)
#pop(index) method mai agar hum koi index  dete hai (agar duplicate hai toh jo first emcounter hoga wahi del )
numbers = [1, 4 , 3 , 6 , 8 , 10]
numbers.pop(4) 
print(numbers)
del numbers[2]
print(numbers)