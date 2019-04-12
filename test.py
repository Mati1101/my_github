# x = 2.8
# print(type(x))
#
# y=3
# print(type(y))
#
# z=2j
# print(type(z))
#
# c=3.5e-4
# print(c)

# x=input("Enter your name:")
# print("Hello," + x)

x = str("ssss www. aaa").upper()
print(x)

my_list = [124125, "tekst", True, 123.44]
my_list2 = [[1,2,3], 2, ['to jest prawda', True]]

print(my_list [0])


for element in reversed(my_list):
    print(element)

print(my_list[-2])

var0=list(range(1,100))
print(var0)

var1=bool("awd")
print(var1)

var2=tuple(my_list)
print(var2)

#pod tuple nie podstawimy nic innego jak niżej

my_list[0]="coś innego"
print(my_list[0])

# print(my_list[0]) #nie da się wrócić spowrotem do tamtej wartości jak myslałem

#słownik (?)
dictionary = {
    "jabłko": "fajny owoc do zjedzenia",
    "tekst": "opis czegoś za pomocą ciagu znaków"
}

print(dictionary["jabłko"])

my_tuple = (2, 214)
print(my_tuple)

for i in my_tuple:
    print(i)

print(my_tuple[0])
print("\n")

for key in dictionary:
    print(key, dictionary[key])

#wyrzuca powtórki - unikalne dane
my_set = {12,124,125,12}
print(my_set)
print("\n")
#list comprehension
my_list_from_list_comp = [i*i for i in range(10)]
print(my_list_from_list_comp)

#drugi sposób
my_numbers = []
for i in range(10):
    my_numbers.append(i*i)
print(my_numbers)

print({i*i for i in range(10)})