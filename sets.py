# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Find the length of the set it_companies
print(len (it_companies))

#Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

#Insert multiple IT companies at once to the set it_companies
multiple_comps={'Twiga','Safaricom','Antara'}
it_companies.update(multiple_comps)
print(it_companies)

#Remove one of the companies from the set it_companies
it_companies.remove('Oracle')
print(it_companies)

#What is the difference between remove and discard
#remove returns an error when an item is not found in the set while discard does not

#Join A and B
#A.update(B)
#print(A)

#Find A intersection B
#A.intersection(B)
#print(A)

#Is A subset of B
print(A.issubset(B))

#Are A and B disjoint sets
print(A.isdisjoint(B))

#Join A with B and B with A

print(A|B)
print(B|A)

#What is the symmetric difference between A and B
print(A.symmetric_difference(B))

#Delete the sets completely
del A
del B

#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
print(len(set(age)))

#Explain the difference between the following data types: string, list, tuple and set
