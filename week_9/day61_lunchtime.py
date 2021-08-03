"""
This question is asked by Apple. You are serving people in a lunch line and need
 to ensure each person gets a “balanced” meal. A balanced meal is a meal where there
  exists the same number of food items as drink items. Someone is helping you prepare
   the meals and hands you food items (i.e. F) or a drink items (D) in the order specified
    by the items string. Return the maximum number of balanced meals you are able to create
     without being able to modify items.
Note: items will only contain F and D characters.

Ex: Given the following items…

items = "FDFDFD", return 3
the first "FD" creates the first balanced meal.
the second "FD" creates the second balanced meal.
the third "FD" creates the third balanced meal.
Ex: Given the following items…

items = "FDFFDFDD", return 2
"FD" creates the first balanced meal.
"FFDFDD" creates the second balanced meal.
"""
# Time O(n)
# Space O(1)
def lunchtime(items):
    count = 0
    total_lunchs = 0
    for el in items:
        if el == "F":
            count -= 1
        else:
            count += 1
        if count == 0:
            total_lunchs += 1
    return total_lunchs

print(lunchtime("FDFDFD"))
print(lunchtime("FDFFDFDD"))