"""
You are going to write a program that will mark a spot on a map with an X.

In the starting code, you will find a variable called map.

This map contains a nested list. When map is printed this is what it looks like, notice the nesting:

[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

This is a bit hard to work with. Ee've used this line of code print(f"{line1}\n{line2}\n{line3}") 
to format the 3 lists to be printed as a 3 by 3 grid, each on a new line.

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

Now it looks a bit more like the coordinates of a real map:

x axis: A, B, C
y axis: 1, 2, 3

"""

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]

map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")
position = input("Enter your coordinates (e.g. B3).") # Where do you want to put the treasure?

# 🚨 Don't change the code above 👆
# Write your code below this row 👇

position = position.upper()

first_coordinate = position [0]
second_coordinate = int(position [1])


if first_coordinate == "A":
  map [second_coordinate - 1][0] = "X"
if first_coordinate == "B":
  map [second_coordinate - 1][1] = "X"
if first_coordinate == "C":
  map [second_coordinate - 1][2] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")