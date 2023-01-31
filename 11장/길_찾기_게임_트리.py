import sys
sys.setrecursionlimit(10**6)


class node:
    def __init__(self, info) -> None:
        self.number = info[2]
        self.data = info[:2]
        self.right = None
        self.left = None


def addnode(root, info):
    if info[0] > root.data[0]:
        if not root.right:
            root.right = node(info)
        else:
            addnode(root.right, info)
    elif info[0] < root.data[0]:
        if not root.left:
            root.left = node(info)
        else:
            addnode(root.left, info)


def preorder(root, order):
    if order != None:
        order.append(root.number)
        preorder(root.left, order)
        preorder(root.right, order)


def postorder(root, order):
    if root != None:
        postorder(root.left, order)
        postorder(root.right, order)
        order.append(root.number)


def solution(nodeinfo):
    nodeinfo = [[*info, idx + 1] for idx, info in enumerate(nodeinfo)]
    nodeinfo = sorted(nodeinfo, key=lambda x: x[1], reverse=True)

    root = node(nodeinfo[0])

    for info in nodeinfo[1:]:
        addnode(root, info)

    preorder_list = []
    preorder(root, preorder_list)

    postorder_list = []
    postorder(root, postorder_list)

    return [preorder_list, postorder_list]
