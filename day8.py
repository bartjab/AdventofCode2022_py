# input data for the task

data_file_input = open('.\\inputs\\input8.txt')
data_input = data_file_input.readlines()
print(data_input)

# part 1

treecount = 0

forest = []
for i in range(len(data_input)):
    forest.append([])
    for j in range(len(data_input[i]) - 1):
        forest[i].append(data_input[i][j])

height = len(forest)
width = len(forest[0])

treecount += 2 * (width + height) - 4       # calculates the trees on the border

for i in range(1, height - 1):
    for j in range(1, width - 1):
        element = forest[i][j]

        isVisibleTop = True
        for y in range(0, i):
            if forest[y][j] >= element:
                isVisibleTop = False
                break

        if isVisibleTop:
            treecount += 1
            continue

        isVisibleBottom = True
        for y in range(i+1, height):
            if forest[y][j] >= element:
                isVisibleBottom = False
                break

        if isVisibleBottom:
            treecount += 1
            continue

        isVisibleLeft = True
        for x in range(0, j):
            if forest[i][x] >= element:
                isVisibleLeft = False
                break

        if isVisibleLeft:
            treecount += 1
            continue

        isVisibleRight = True
        for x in range(j+1, width):
            if forest[i][x] >= element:
                isVisibleRight = False
                break

        if isVisibleRight:
            treecount += 1
            continue


for i in range(len(forest)):
    for j in range(len(forest[i])):
        print(forest[i][j], end='')
    print()

print(treecount)

# part 2

highestScenicScore = 0
for i in range(1, height - 1):
    for j in range(1, width - 1):
        element = forest[i][j]

        topRange = 0
        for y2 in range(i-1, -1, -1):
            topRange += 1
            if forest[y2][j] >= element:
                break

        bottomRange = 0
        for y2 in range(i+1, height):
            bottomRange += 1
            if forest[y2][j] >= element:
                break

        leftRange = 0
        for x2 in range(j-1, -1, -1):
            leftRange += 1
            if forest[i][x2] >= element:
                break

        rightRange = 0
        for x2 in range(j+1, width):
            rightRange += 1
            if forest[i][x2] >= element:
                break

        scenicScore = topRange * bottomRange * leftRange * rightRange
        if highestScenicScore < scenicScore:
            highestScenicScore = scenicScore

print(highestScenicScore)
