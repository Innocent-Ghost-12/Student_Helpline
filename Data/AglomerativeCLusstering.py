import math

dataset = [[0.40, 0.53], [0.22, 0.38], [0.35, 0.32], [0.26, 0.19], [0.08, 0.41], [0.45, 0.30]]
# diff = []
l = []

diff = [[0,9,3,6,11],[9,0,7,5,10],[3,7,0,9,2],[6,5,9,0,8],[11,10,2,8,0]]

# for i in range(len(dataset)):
#     diff.append([])
#     for j in range(len(dataset)):
#         diff[i].append(math.sqrt((dataset[i][0] - dataset[j][0]) ** 2 + (dataset[i][1] - dataset[j][1]) ** 2))


for i in range(len(diff)):
    for j in range(len(diff[i])):
        if diff[i][j] == 0:
            diff[i][j] = 999
ITERATION = 0


while (len(diff) > 1):
    print("ITERATION:", ITERATION)
    MIN = min(min(diff,key=min))

    for i in range(len(diff)):
        for j in range(len(diff[i])):
            if diff[i][j] == MIN:
                m = i
                n = j
                break
    mergeRow1 = [k for k in diff[m]]
    mergeRow2 = [k for k in diff[n]]

    for i in range(len(mergeRow1)):
        l.append(max(mergeRow1[i], mergeRow2[i]))

    for i in diff:
        data1 = i[n]
        data2 = i[m]

        i.remove(data1)
        i.remove(data2)


    if n > m:
        del diff[n]
        del diff[m]
        del l[n]
        del l[m]
    else:
        del diff[m]
        del diff[n]
        del l[m]
        del l[n]

    for i in range(len(diff)):
        diff[i].append(l[i])

    l.append(999)

    diff.append([i for i in l])

    print("Merged rows are: ", m + 1, ' ', n + 1)
    print("Distance Table after merge: ")
    for i in diff:
        print(i)
    print()
    l.clear()
    mergeRow1.clear()
    mergeRow2.clear()
    ITERATION += 1
