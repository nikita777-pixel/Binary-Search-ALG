"""Nikita Volodin PR"""

import random # Import library random here.

# Variable for created Sorted Massive here:

mas = []
mas_len = 10
min_nam_to_mas = 0
max_nam_to_mas = 100

# Realization Created Rundom Number to massive here:

for i in range(mas_len):
    mas.append(random.randint(min_nam_to_mas, max_nam_to_mas))

print("Don't Sorted massive: " + str(mas))

# Realization BubbleSorted Alg here:

for i in range(mas_len):
    for j in range(mas_len - 1):
        # Chekc if mas[0] > mas[1]:

        if mas[j] > mas[j + 1]:
            # Swap to massive here:

            mas[j], mas[j + 1] = mas[j + 1], mas[j]

print("Sorted Massive : " + str(mas))

def BinarySearch(mas, iskat, start, stop):
    # Realization Binary Search here:

    if start > stop: # Check if to massive is not IsKut Number here:
        return False

    else:
        mid = (start + stop) // 2 # Created mid (Variable) mid on mas.
        if iskat == mas[mid]: # Check if mid == IsKut Number.
            return mid
        elif iskat < mas[mid]: # Check if IsKat < mid : we looking on left board massive here:
            return BinarySearch(mas, iskat, start, mid - 1) # Return function but stop == mid - 1 i looking to left board.
        else: # If not oll. IsKat number to Right board:
            return BinarySearch(mas, iskat, mid + 1, stop) # Return Function but start == mid + 1 i looking to Right Board.

# Created Variable for Binary Search here:

iskat = 10
start = 0
stop = len(mas)

binary_search = BinarySearch(mas, iskat, start, stop)

print('Looking Number ' + str(iskat))

if binary_search == False: # Check if to massive is not this number:
    print('Number to massive not!')
else: # Else this massive have this number:
    print("Massive have " + str(iskat) + " This number is to massive!")







