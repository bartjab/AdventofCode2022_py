# input data for the task

data_file_input = open('.\\inputs\\input6.txt')
data_input = data_file_input.read()
print(data_input)

# part 1

for i in range(4, len(data_input)):
    marker = data_input[(i-4):i]
    is_sop = True                       # is_sop - is start-of-packet
    for char in marker:
        if marker.count(char) > 1:
            is_sop = False
            break
    if is_sop:
        print(i)
        break

# part 2

for i in range(14, len(data_input)):
    marker = data_input[(i-14):i]
    is_som = True                       # is_som - is start-of-message
    for char in marker:
        if marker.count(char) > 1:
            is_som = False
            break
    if is_som:
        print(i)
        break
        