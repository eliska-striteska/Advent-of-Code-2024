# Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number 
# with the second-smallest right number, and so on.
# Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances.
# To find the total distance between the left list and the right list, add up the distances between all of the pairs you found.

left_list = []
right_list = []

with open('input.txt', encoding="utf-8") as file:
    for line in file:
        place_ids = line.split()
        left_list.append(place_ids[0].strip())
        right_list.append(place_ids[1].strip())

left_list_sorted = sorted(left_list)
right_list_sorted = sorted(right_list)

paired_ids = list(zip(left_list_sorted, right_list_sorted))

#print(paired_ids[:5])

def calculate_distance(tuple):
    distance = abs(int(tuple[0]) - int(tuple[1]))
    return distance

distances = []
for tuple in paired_ids:
    distance = calculate_distance(tuple)
    distances.append(distance)

total_distance = sum(distances)
print(total_distance)


