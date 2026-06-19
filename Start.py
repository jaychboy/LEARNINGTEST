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
