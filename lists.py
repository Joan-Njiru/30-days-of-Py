#Declare an empty list
empty=[]

#Declare a list with more than 5 items
fruits=["mangoes","apples","pears","pineapples","pomegranate","passion"]

#Find the length of your list
print(len(fruits))

#Get the first item, the middle item and the last item of the list
print(fruits[0])
middle_index=(len(fruits)-1)//2
print(fruits[middle_index])
print(fruits[-1])

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types=["Joan",23,163.5,"to-be-married","64,Runyenjes"]

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, 
# Apple, IBM, Oracle and Amazon.

it_companies=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
#Print the list using print()
print(it_companies)

#Print the number of companies in the list
print(len(it_companies))

#Print the first, middle and last company
print(it_companies[0])
mid=(len(it_companies)-1)//2
print(it_companies[mid])
print(it_companies[-1])

#Print the list after modifying one of the companies
it_companies[5]="PiedPiper"
print(it_companies)

#Add an IT company to it_companies
it_companies.append("Tesla")
print(it_companies)

#Insert an IT company in the middle of the companies list
it_companies.insert(mid,"Meta")
print(it_companies)

#Change one of the it_companies names to uppercase (IBM excluded!)
print(it_companies[3].upper())

#Join the it_companies with a string '#;  '
hash_companies='#'.join(it_companies)
print(hash_companies)

#Check if a certain company exists in the it_companies list.
print("Amazon" in it_companies)

#Sort the list using sort() method

it_companies.sort()
print(it_companies)

#Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

#Slice out the first 3 companies from the list
print(it_companies[0:3])

#Slice out the last 3 companies from the list
print(it_companies[-1:-4])

#Slice out the middle IT company or companies from the list

#Remove the first IT company from the list
del it_companies[0]
print(it_companies)

#Remove the middle IT company or companies from the list

#Remove the last IT company from the list
del it_companies[-1]
print(it_companies)

#Remove all IT companies from the list
it_companies.clear()
print(it_companies)

#Destroy the IT companies list
del(it_companies)

#Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print(front_end)



