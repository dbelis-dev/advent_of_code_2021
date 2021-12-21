import sys
import os
import pprint

tree = {
    "start": []
}
path_array = []

def main():
    global pp
    pp = pprint.PrettyPrinter(indent=4)
    filepath = './input_file-example'

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    ### Read the input into an array of integers
    read_array_in(filepath)
    # path_array.append("start")
    traverse_tree("start")


    print("================================================================")
    # print("Result: {}".format(sum_flashes))

def traverse_tree(node):
    path_array.append(node)
    children = tree[node]
    for child in children:
        print(child)
        if child == "end":
            print("End reached")
            print(path_array)
            break
        if child in tree:
            if child not in path_array or child.isupper():
                print("   Traversing")
                traverse_tree(child)
            else:
                print("   Already checked! Skipping")
        else:
            print("   Not in tree! Skipping")
            continue


### Iterate over the lines in the file
def read_array_in(filepath):
    with open(filepath, 'r') as fp:
        for line in fp.readlines():
            line = line.rstrip()
            parent_, child_ = line.split('-')
            # print(parent_, child_)
            if parent_ not in tree:
                tree[parent_] = [child_]
            else:
                tree[parent_].append(child_)
            # if child_ != "end":
            if child_ not in tree:
                tree[child_] = [parent_]
            else:
                tree[child_].append(parent_)
    print(tree)

if __name__ == '__main__':
    main()