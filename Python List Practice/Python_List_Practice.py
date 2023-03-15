import random
 
colors = ["Blue", "Teal", "Magenta", "Green", "Red"]
print(colors[0])
print(colors [2])
print(colors[4])
colors.append("Baby Blue")
print(colors)

paychecks = [500, 470, 800, 780]
total = 0

for i in range(len(paychecks)):
    total += paychecks[i]

print(total)


types = int(input("How many types of foods would you like to take to mars?: "))
foods = []
for i in range(types):
    mars = input("What food would you like to take to mars?")
    foods.append(mars)
    print(foods)
