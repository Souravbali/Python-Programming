student = {'Name':'Sourav',1:'id','Department':'BCA'}
print(student) #print all the keys and values together 
# Acess the element of the dictionary 
element = student['Name'] 
print(element)
# with the help of key , we can access the value of dictionary
'''
print all the keys 
'''
print(student.keys()) # key method help to print all list of  the keys values 
print(student.values()) #value method help to print all list of the vlaues 
print(student.items()) #item method help to print all the list of both keys and values in the form of tuple 

# how to add element in the dictionary
student['college'] = 'miet'
print(student)

studentmarks = {'English':100,'Math':100}
student.update(studentmarks)
print(student)

# remove the element in the dictionary 
student.pop('college')
print(student)
student.popitem () # cut the last element 
print(student)
# .clear() method clear all the dictionary 