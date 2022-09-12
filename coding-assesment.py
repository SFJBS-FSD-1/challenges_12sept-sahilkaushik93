# Challenge ************************************************************************************************************
# Write a function that takes a natural number as input and outputs the number of digit in it.Conversion of number
# to string is not allowed

# solution:-
# step1: take input from user
# step2: divide the number by 10 and convert the quotient into interger type
# step3: if quotient is not 0, update count of digit by 1
# step4: if quotient is 0, stop the count

def no_of_digits():
    number_input = int(input("Enter your number to find digits in it: "))
    count_of_digits = 0
    while number_input > 0:
        number_input = int(number_input / 10)
        count_of_digits += 1
    return ("Number of digits: ", count_of_digits)

print("Challenge 1 ***************************************************************************************************** ")
print(no_of_digits())

# Challenge ************************************************************************************************************
# 2: Write a function that takes a natural number as input and outputs the reverse of that number.Conversion of number
# to string is not allowed

# solution:-
# step1: Initialize reverse_num = 0
# step2: Loop while num>0
#  a) Multiply reverse_num by 10 and add remainder of num divide by 10 to reverse_num (reverse_num = reverse_num*10 + num%10)
#  b) Divide num by 10
# return reverse_num

def reverse_number():
    num_2 = int(input("Enter your number to print reverse of it: "))
    reverse_num = 0
    while num_2 > 0:
        remainder = num_2 % 10
        reverse_num = reverse_num * 10 + remainder % 10
        num_2 = num_2 // 10

    return ("Reverse of num is as following: ", reverse_num)

print("Challenge 2 ***************************************************************************************************** ")
print(reverse_number())


# Challenge
# 3: Write a function where user will enter a natural number as input and output returns the number of zeroes in the
# end of the factorial of that number.Conversion of number to string is not allowed

def count_zero():
    num_3 = int(input("Enter number to check zeroes: "))
    fact = 1
    count = 0
    for i in range(1, num_3):
        fact = fact * i
    while fact > 9:
        count += int(fact % 10 == 0)
        fact //= 10

    return ("No of zeroes in the factorial of number: ", count)

print("Challenge 3 ***************************************************************************************************** ")
print(count_zero())

# Challenge
# 4: list1 = ["India", "England", "Spain"]
# list2 = ["Delhi", "London", "Madrid"]
# Write your own function that takes list1 and list2 as inputs and returns a dictionary like
# dict1 = {“India”: “Delhi”, “England”:”London”, “Spain”:”Madrid”}

# solution
# step1: parse through list 1 and list 2 by using for loop, where i & j should be respective index numbers of elements in the lists
# step2: wherever i & j matches populate it in new dictionary as key and value pair

list1 = ["India", "England", "Spain"]
list2 = ["Delhi", "London", "Madrid"]

def make_dictionary(list1, list2):
    dict1 = {}
    for i in range(len(list1)):
        for j in range(len(list2)):
            if i == j:
                dict1[list1[i]] = list2[j]

    return ("Dictionary output: ", dict1)

print("Challenge 4 ***************************************************************************************************** ")
print(make_dictionary(list1=list1, list2=list2))


# Challenge
# 5:
# Given places = {(“19.07'53.2”, “72.54'51.0”): "Mumbai",(“28.33'34.1”, “77.06'16.6”): "Delhi"}
#
# Write code to create a new dictionary using given dictionary
# city = {"Mumbai": {“Latitude”: “19.07'53.2” , “Longitude”: “72.54'51.0”},
# “Delhi”: {“Latitude”: “28.33'34.1” , “Longitude”: “77.06'16.6”}}

# given_places = {("19.07'53.2”, “72.54'51.0”): "Mumbai", ("28.33'34.1", "77.06'16.6"): "Delhi"}
places = {("19.07'53.2", "72.54'51.0"): "Mumbai", ("8.33'34.1", "77.06'16.6"): "Delhi"}

city_pos = {}
city = {}

for i,j in places.items():
    city_pos["Latitude"] = i[0]
    city_pos["Longitude"] = i[1]
    city[j] = city_pos


# print(city_pos)
print("Challenge 5 ***************************************************************************************************** ")
print(city)

# Challnege
# 6: Given mylist = [3, 5, 4, 6, 9, 10, 2, 8, 7, 1]
# Using for loop find the sum of all even numbers in mylist

mylist = [3, 5, 4, 6, 9, 10, 2, 8, 7, 1]


def sum_of_even_num(list):
    even_sum = 0
    for i in list:
        if i % 2 == 0:
            even_sum = even_sum + i

    return ("Sum of all even numbers is: ", even_sum)

print("Challenge 6 ***************************************************************************************************** ")
print(sum_of_even_num(list = mylist))






