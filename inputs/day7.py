# input data for the task

data_file_input = open('.\\inputs\\input7.txt')
data_input = data_file_input.readlines()
print(data_input)

# part 1


class Tree:

    def __init__(self, data=['dir', '/'], parent=None):
        self.data = data
        self.parent = parent
        self.children = []

    def dir_size(self):
        size = 0
        for child in self.children:
            if child.data[0].isdigit():
                size += int(child.data[0])
            else:
                size += child.dir_size()
        return size

    def read_tree(self, level=0):
        if self.data[0] == 'dir':
            print('  ' * level + '--' + self.data[0] + ' ' + self.data[1] + '(dir size: ' + str(self.dir_size()) + ')')
        else:
            print('  ' * level + '--' + self.data[1] + ' ' + self.data[0])
        for child in self.children:
            child.read_tree(level + 1)


filesystem = Tree()
current_parent = filesystem

for i in range(1, len(data_input)):                     # constructing a directory tree
    line_info = data_input[i].split()
    # print(line_info)
    if line_info[0] == '$':
        if line_info[1] == 'cd':
            if line_info[2] == '..':
                current_parent = current_parent.parent
            else:
                for k in current_parent.children:
                    if k.data[1] == line_info[2]:
                        current_parent = k
                        break
    else:
        current_parent.children.append(Tree(line_info, current_parent))

filesystem.read_tree()
print(filesystem.dir_size())

# counts the amount of directories with a size of at most 100000 and sums their sizes
def dir_count(dir_tree):
    count_and_total_size = [0, 0]
    size = dir_tree.dir_size()
    if size <= 100000:
        count_and_total_size[0] += 1
        count_and_total_size[1] += size
    for child in dir_tree.children:
        if child.data[0] == 'dir':
            count_and_total_size[0] += dir_count(child)[0]
            count_and_total_size[1] += dir_count(child)[1]
    return count_and_total_size


print('There are ' + str(dir_count(filesystem)[0]) + ' directories of size 100000 and lower and their total sum is ' + str(dir_count(filesystem)[1]))

# part 2

size_required = 30000000 - (70000000 - filesystem.dir_size())
print('Required additional free space: ' + str(size_required))

# this function checks which directory is needed to delete
# min_size_req argument determines the lowest required free space
def read_dir_sizes(dir_tree, dir_list=[]):
    dir_list.append(dir_tree.dir_size())
    for child in dir_tree.children:
        if child.data[0] == 'dir':
            read_dir_sizes(child)
    return dir_list


curr_min_size = 70000000
dir_size_list = read_dir_sizes(filesystem)
for item in dir_size_list:
    if size_required <= item < curr_min_size:
        curr_min_size = item

print(dir_size_list)
print(curr_min_size)
