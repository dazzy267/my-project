age = 35

#age limit
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65

#the lines determine the bus fare price
concession_ticket = 1.25
adult_ticket = 2.50

if age < free_up_to_age:
    ticket = 0
elif age < child_up_to_age:
    ticket = 1.25
elif age > senior_from_age:
    ticket = 1.50
else:
    ticket = 2.50

message = "somebody who is {} years old will pay ${} to ride the bus".format(age, ticket)
print(message)

cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities:
    print(city.title())
print('Done!')

print(cities)
for city in cities:
     city = city.title()
     print(city)


names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for name in names:
    name = name.lower().replace(" ", "_")

print(names)

card_deck = [4,11,8,5,13,2,8,10]
hand =[]
while sum(hand) <= 17:
    hand.append(card_deck.pop())
    print(sum(hand))

number = 6
current = 1
product = 1

while current <= number:
    product *= current
    current += 1
    print(product)

#using a for loop for finding the factorial
number =  6
product = 1
for i in range(1, number + 1):#we used number + 1 because range six would have stopped in 5
    product *= i
    print(product)

#COUNT BY
start_num = 4
end_num = 100
count_by = 4
break_num = start_num
while break_num <= end_num:
    break_num += count_by
    print(break_num)

start_num = 4
end_num = 100
count_by = 4
for i in range(4,100,4):
    print(i)

start_num = 4
end_num = 100
count_by = 6
if start_num > end_num:
    result = 'Oops! the start number was greater than the end_num. Please try again.'
else:
    break_num = start_num
    while break_num <= end_num:
        break_num += count_by
    result = break_num
print(result)

#finding the square using while loop
limit = 40
num = 0
while (num + 1)**2 < 40:
    num += 1
    print(num)
result = num**2

num = 0
for i in range(1,7):
    num = (num + 1)**2
    num = i
    result = num**2
print(result)


num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

count_odd = 0
list_sum = 0
i = 0
len_num_list = len(num_list)

while (count_odd < 5) and (i < len_num_list): 
    if num_list[i] % 2 != 0:
        list_sum += num_list[i]
        count_odd += 1
    i += 1

print ("The numbers of odd numbers added are: {}".format(count_odd))
print ("The sum of the odd numbers added is: {}".format(list_sum))

manifest = [("bananas",15), ("mattresses",24), ("dog kennels", 42), ("machine",120), ("cheese",5)]
weight = 0
item = []
for cargo in manifest:
    if weight >= 100:
        print('the limit i can carry')
        break
    else:
        item.append(cargo[0])
        weight += cargo[1]
print(weight)
print(item)

check_prime = [26,39,51,53,57,79,85]
for num in check_prime:
    for i in range(2,num):
        if (num % i) == 0:
            print(" {} is  not a prime number, because {} is a factor of {}".format(num,i,num))
            break
        if i == num -1:
            print(" {} is  a prime number".format(num))
items = ['banana', 'mattresses', 'dog kennels', 'machine', 'cheeses']
weight = [15,34,42,120,5]
list = (list(zip(items, weight)))
print(list)

for cargo in zip(items,weight):
    print(cargo[0], cargo[1

