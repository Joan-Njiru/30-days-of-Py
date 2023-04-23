#Create an empty tuple
my_tuple=()

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
my_brothers=("Ian","Ted","Munene")
print(my_brothers)
my_sisters=("Kathomi","Carol")
print(my_sisters)

#Join brothers and sisters tuples and assign it to siblings
my_siblings=my_brothers+my_sisters
print(my_siblings)

#How many siblings do you have?
no_of_siblings=len(my_siblings)
print(no_of_siblings)

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
my_siblings=list(my_siblings)
my_siblings.extend(["Fredrick","Florence"])
my_family=tuple(my_siblings)
print(my_family)

#Unpack siblings and parents from family_members
for i in range(len(my_family)):
    print(my_family[i])

#Create fruits, vegetables and animal products tuples. Join the three tuples 
# and assign it to a variable called food_stuff_tp.
fruits=("mangoes","oranges","pineapples","pomegranate","passion")
vegetables=("onions","mangoes","tomatoes","potatoes","ngwaci")
animal_products=("cheese","yoghurt","milk","meat","eggs")
food_stuff_tp=fruits+vegetables+animal_products
print(food_stuff_tp)

#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt=list(food_stuff_tp)
print(food_stuff_lt)

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
mid=len(food_stuff_lt)//2
food_stuff_lt.pop(mid)
print(food_stuff_lt)

#Slice out the first three items and the last three items from food_staff_lt list
#food_stuff_lt[0:4]
#print(food_stuff_lt)

#Delete the food_staff_tp tuple completely
del food_stuff_tp

#Check if an item exists in tuple:
#Check if 'Estonia' is a nordic country
#Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)

