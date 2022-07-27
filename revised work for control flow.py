seasons = ['winter', 'summer', 'fall', 'spring', ' nope']
for season in seasons:
    if season == 'fall':
        print('harvest the garden')
        print(season)
    elif season == 'winter':
        print('stay indoors')
        print(season)
    elif season == 'summer':
        print('water the garden')
        print(season)
    elif season == 'spring':
        print('plant the garden')
        print(season)
    else:
        print("don't know the season ")

weight = 55
height = 164
if 18.5 <= weight or height**2 < 25:
    print("BMI is considered 'normal'")

cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities:
    print(city.title())

capitalized_cities = []
for city in cities:
     capitalized_cities.append(city.title())

print(capitalized_cities)

print(cities)
for i in range(len(cities)):
    print(cities[i].title())

for i in range(len(cities)):
    cities[i] = cities[i].title()

print(cities)
capitalize = []
sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
for each_word in sentence:
    capitalize.append(each_word.title())
names = ["joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []
for name in names:
    usernames.append(name.lower().replace(" ", "_"))
    print(usernames)

for i in range(len(usernames)):
    usernames[i] = usernames[i].title()

tokens = ['<greetings>', 'Hello world', '<Greetings>']
count = 0
for word in tokens:
    if word[0] == '<' and word[-1] == '>':
        count += 1

book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}
for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1

print("\niteratiing using counter")
    
counter = {}
for word in book_title:
    counter[word] = counter.get(word,0) + 1
    print(counter)


cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }
for keys, values in cast.items():
    print("Actors: {}      Names: {}".format(keys,values))

print('\nCounting Number of fruit basket_item')
result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
for items, weights in basket_items.items():
    if items in fruits:
        result += weights
        print(result)
manifest = [
            ("bananas", 15),
            ("mattresses", 34),
            ("dog kennels", 42),
            ("machine", 120),
            ("cheeses", 5)
            ]
items = ['bananas', 'mattresses', 'dog kennels', 'machine', 'cheeses']
weight = [15, 34, 42, 120, 5]
for cargo in zip(items, weight):
    print(cargo[0], cargo[1])
print('\n')

things, mass = zip(*manifest)
print(things, mass)
