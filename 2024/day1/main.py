with open("2024/day1/input.txt", "r") as f:
    locations = f.readlines()


left = []
right = []

for location in locations:
    left.append(location.split()[0])
    right.append(location.split()[1])


def difference(left, right):
    left.sort()
    right.sort()

    diff = []
    for i in range(len(locations)):
        diff.append(abs(int(left[i]) - int(right[i])))

    return sum(diff)


def similarity(left, right):
    res = 0
    for i in range(len(locations)):
        res += int(left[i]) * int(right.count(left[i]))
        # print(int(left[i]) * int(right.count(left[i])))
    return res


print(difference(left, right))

print(similarity(left, right))
