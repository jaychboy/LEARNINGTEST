"""
left = " Python"
right = "Python "
tab = "Python"
both = " Python "
undercased = "python"

print(undercased.title())
print(undercased.upper())

print(undercased.strip().lower().strip())

print(left.lstrip())
print(right.rstrip())
print(both.strip())

print(f"\t{tab}")
print("Hello,\nWorld")
print("The things:,\n\tThe\n\tPreceding")

website = "https://wikipedia.com"
print(website.removeprefix("https://"))


x, y, z = "x", "y", "z"
MAX_CONNECTIONS = 500
"""
"""
list = ["Henry Adams", "Jayden Chen", "Kyle Liang"]

first = list.pop()
print(f"Welcome to the dinner, {first}")

second = list.pop()
print(f"Welcome to the dinner, {second}")

third = list.pop()
print(f"Welcome to the dinner, {third}")

invited_in_total = []
invited_in_total.insert(0, first)
invited_in_total.insert(1, second)
invited_in_total.append(third)

list.insert(0, "Jason Yu")
list.insert(1, "Jason Jiarui Yu")
list.append("Damon Lin")

first = list.pop()

print(f"Welcome to the dinner, {first}")

second = list.pop()
print(f"Welcome to the dinner, {second}")

third = list.pop()
print(f"Welcome to the dinner, {third}")

invited_in_total.insert(3, first)
invited_in_total.insert(4, second)
invited_in_total.append(third)

print(f"{invited_in_total}")
"""

""""
new_list = ["Henry Adams", "Jayden Chen", "Kyle Liang", "Jason Yu"]

new_list.sort()
print(new_list)

new_list.sort(reverse=True)
print(new_list)

sorted = sorted(new_list)
print(sorted)

new_list.sort()
print(new_list)

new_list.reverse()
print(new_list)

new_list.sort()
print(new_list)


length = len(new_list)
print(length)

list1 = []
list1.insert(0, "Missisipi River")
list1.insert(1, "Yangtze River")
list1.insert(2, "Hudson River")
list1.insert(3, "East River")
list1.append("Shing Mun River")

print(list1[1].title())

print(list1)

item = list1.pop(4)

list1.append(item)

print(list1)

del list1[4]

list1.append(item)

print(len(list1))

list1.remove("Shing Mun River")

print(list1)
print(len(list1))

list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)

list1.sort()

print(list1)

list1.reverse()
print(list1)

print(sorted(list1))

list1.sort()

print(list1)
"""

"""
names = ["Henry Adams", "Jayden Chen", "Kyle Liang", "Jason Yu"]

for name in names:
    print(f"{name.title()}, thet thing was that was great!")
    print(f"Articulate more the, {name.title()}! \n")

print("Great Articulation!")

toppings = ["Pepporoni, Sausage, Bell Pepper(s), Pineapple"]

for topping in toppings:
    print(f"{topping.title()} Pizza, is a variation of pizza articulated, accordingly.")

for value in range(1,5):
    print(value)

even_numbers = list(range(2,11,2))
print(even_numbers)

squared_list = []

for value in range(1,11):
    square = value ** 2
    squared_list.append(square)

print(squared_list)

square_list = []

for value in range(1,11):
    square_list.append(value ** 2)

print(square_list)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(min(digits))

print(max(digits))

print(sum(digits))

squares = [value ** 2 for value in range(1,11)]

print(squares)

cubes = [cube ** 3 for cube in range(1,11)]

print(cubes)
"""

"""
programming_languages = ["Javascript", "Python", "C++", "Java", "C#"]

print(programming_languages[1:4])

print(programming_languages[:5])

print(programming_languages[1:])

print(programming_languages[-4:])

print("\nHere are the first four Programming Languages.\n")

for programming_language in programming_languages[:4]:
    print(f"These are the four Programming Languages, {programming_language}")

programming_second = ["Python", "Javascript", "C++", "Java"]

programming_first = programming_second[:]

programming_first.append("Python 3.14")

programming_second.append("Python 3.14")
                         

print("\nThe programming languages are: \n")
print(programming_first)

print("\nThe programming languages are also alternatively: \n")
print(programming_second)

print(f"The first three items in the list are:. {programming_languages[:3]}")

print(f"Three items from the middle of the list are:. {programming_languages[1:4]}")

print(f"The last three items in the list are:. {programming_languages[-3:]}\n")



toppings = ["Pepporoni", "Sausage", "Bell Pepper(s)", "Pineapple"]

modern_toppings = toppings[:]

toppings.append("Tomato")

modern_toppings.append("Bacon")

for topping in toppings:
    print(f"The toppings incorporated are;, {topping}\n")

for modern_topping in modern_toppings:
    print(f"The modern toppings incorporated are also;, {modern_topping}\n")

dimensinons = (200, 50)
print("Original Dimensions:")
for dimension in dimensinons:
    print(dimension)

dimensions = (400,100)

print("\nModified Dimensions:")
for dimension in dimensions:
    print(dimension)

print("\nThis is the current menu.\n")
foods = ("Spring Rolls", "Broccoli", "Rice", "Fish", "Dumplings")
for food in foods:
    print(food)

print("\nThis is the new menu.\n")
new_foods = ("Crab", "Lobster", "Broccoli", "Rice", "Fish")
for food in new_foods:
    print(food)
"""

"""
abbreviated_full = ["jfk", "hong kong international airport", "beijing capital international airport", "shanghai pudong international airport"]

for abbreviate in abbreviated_full:
    if abbreviate == "jfk":
        print(abbreviate.upper())
    else:
        print(abbreviate.title())

requested_topping = "mushrooms"

if requested_topping != "anchovies":
    print("Hold the anchovies!")

age_0 = 22
age_1 = 18

print((age_0 >= 21) and (age_1 >= 21))

age_1 = 22

print((age_0 >= 21) and (age_1 >= 21))

print((age_0 >= 21) or (age_1 >= 21))

age_0 = 18
age_1 = 18

print((age_0 >= 21) or (age_1 >= 21))

users = ["Henry", "Jayden", "Kyle", "Damon"]

user = "Jason"

if user not in users:
    print(f"{user.title()}, you are in.")

age = 17

if age >= 18:
    print("You are old enough to vote")
    print("Have you registered to vote yet?")
else:
    print("Sorry you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")


age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(price)



requested_toppings = ["mushrooms", "extra cheese"]

if "mushrooms" in requested_toppings:
    print("\nAdding mushrooms.")
elif "pepperoni" in requested_toppings:
    print("\nAdding pepperoni.")
elif "extra cheese" in requested_toppings:
    print("\nAdding extra cheese.")


print("\nFinished making your pizza!")

requested_toppings = ["mushrooms", "extra cheese"]

if "mushrooms" in requested_toppings:
    print("\nAdding mushrooms.")
if "pepperoni" in requested_toppings:
    print("Adding pepperoni.")
if "extra cheese" in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

color = "yellow"

if color == "green":
    print("You just earned five points!")
if color == "yellow":
    pass
if color == "red":
    pass

color = "green"

if color == "green":
    print("You just earned five points!")
if color == "yellow":
    print("You just earned 10 points!")
if color == "red":
    print("You just earned 10 points!")

if color == "green":
    print("You just earned five points!")
else:
    print("You just earned ten points!")

if color == "green":
    print("You just earned 5 points")
elif color == "yellow":
    print("You just earned 10 points")
else:
    print("You just earned 15 points")

requested_toppings = ["Mushrooms", "Green Peppers", "Extra Cheese"]

for requested_topping in requested_toppings:
    if requested_topping == "Green Peppers":
        print("Sorry, we are out of green peppers right now")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

print("\n")

avalaible_toppings = ["mushrooms", "olives", "green peppers",
                      "pepperoni", "pineapple", "extra cheese"]

requested_toppings = ["mushrooms", "french fries", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in avalaible_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we dont have {requested_topping}")

print("\nFinished making your pizza!")

print("\n")

current_users = ["Henry Adams", "Jayden Chen", "Kyle Liang", "Jason Yu", "Admin"]

new_users = ["Henry", "Jayden", "Kyle", "Jason", "admin"]

if users:
    for user in users:
        if user == "admin":
            print("Hello admin, would you like tot see a status report?")
        else:
            print(f"Hello {user}")
else:
    print("We need to find somer users!")

print("\n")

for new_user in new_users:
    if new_user in current_users:
        print("Please enter a new username.")
    elif new_user.title() in current_users:
        print("Please enter a new username")
    elif new_user.upper() in current_users:
        print("Please enter a new username.")
    elif new_user.lower() in current_users:
        print("Please enter a new username.")
    else:
        print("This username is still available.")

print("\m")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num == 1:
        print(str(num) + "st")
    elif num == 2:
        print(str(num) + "nd")
    elif num == 3:
        print(str(num) + "rd")
    else:
        print(str(num) + "th")

"""

alien_0 = {"color": "green", "points": 5}

print(alien_0["color"])
print(alien_0["points"])

alien_0 = {"color": "green", "points": "5"}

new_points = alien_0["points"]
print(f"You just earned {new_points} points!")

alien_0 = {"color": "green", "points": 5}
print(alien_0)

alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

alien_0 = {}
alien_0["color"] = "green"
alien_0["points"] = 5
print(alien_0)

alien_0 = {"color": "green"}
print(f"The alien is {alien_0["color"]}")
alien_0 = {"color": "yellow"}
print(f"The alien is {alien_0["color"]}")

