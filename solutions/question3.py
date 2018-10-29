class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def ser(node,flag):
    #     global string, q
    string = ''
    if node is None:
        if flag == 'l':
            string +="L"
        else:
            string += "R"
        string += "None"
        string += ','
        return string
    #     else:
    string += node.val
    string += ','

    string += ser(node.left,'l')
    string += ser(node.right,'r')
    return string


def serialize(node):
    global string
    string = ''
    q = []
    st = ser(node,'l')
    # print(st)
    return st


def des(full, currentNode):
    global i
    #     i+=1
    if i >= len(full) - 1:  # or full[i] == 'None'
        #         currentNode=None
        return

    #     i+=1
    # set node.l
    if i >= len(full) - 1 or full[i] == 'LNone':
        currentNode.left = None  # if none don't go more left
        i += 1
    #         print()
    elif i <= len(full) - 1 and full[i] != 'RNone':
        currentNode.left = Node(full[i])
        i += 1  # next ones
        des(full, currentNode.left)

    # set node.r
    #     i+=1
    if i>= len(full) - 1 or full[i] == "RNone":
        # i += 1
        currentNode.right = None  # if none don't go more right
        i += 1
        return
    elif i + 1 <= len(full) - 1 and full[i] != 'LNone':
        # i += 1
        currentNode.right = Node(full[i])
        i += 1  # next ones
        des(full, currentNode.right)


def deserialize(string):  # to tree
    global i
    i = 0
    full = string.split(',')
    #     print(full)
    root = Node(full[0])
    i += 1
    des(full, root)
    return root


node = Node('root', Node('left', Node('left.left')), Node('right', None, Node('right.right')))
s = serialize(node)
# print("S:{}".format(s))
print(deserialize('root,left,left.left,LNone,RNone,RNone,right,LNone,right.right,LNone,RNone').right.right.val)

assert deserialize(serialize(node)).left.left.val == 'left.left'
assert deserialize(serialize(node)).right.right.val == 'right.right'

