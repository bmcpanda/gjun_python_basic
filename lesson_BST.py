import random


class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left_tree = None
        self.right_tree = None

    def insert(self, data):
        if self.data != data:  # Is root node != data?
            if data < self.data:  # insert to left_tree
                if self.left_tree:
                    self.left_tree.insert(data)
                else:
                    self.left_tree = BinarySearchTree(data)
                # return self.left_tree
            else:  # insert to right_tree
                if self.right_tree:
                    self.right_tree.insert(data)
                else:
                    self.right_tree = BinarySearchTree(data)
                # return self.right_tree

    def delete(self, data):
        if data < self.data:
            if self.left_tree:
                self.left_tree = self.left_tree.delete(data)
            else:
                print(f"Delete {data} fail: data not found")
            result_tree = self
        elif data > self.data:
            if self.right_tree:
                self.right_tree = self.right_tree.delete(data)
            else:
                print(f"Delete {data} fail: data not found")
            result_tree = self
        else:
            # data==self.data
            # 找人遞補當前空缺
            # 無子樹
            if self.left_tree == self.right_tree == None:
                result_tree = None
            elif self.left_tree == None and self.right_tree != None:  # only right tree
                result_tree = self.right_tree
            elif self.left_tree != None and self.right_tree == None:  # only left tree
                result_tree = self.left_tree
            else:
                # left and right tree, use right min to substitute

                substitute = self.right_tree  # 右子樹根節點
                while substitute.left_tree != None:
                    substitute = substitute.left_tree

                self.data = substitute.data
                self.right_tree = self.right_tree.delete(substitute.data)
                result_tree = self
        return result_tree

    def search(self, data):
        if data < self.data:
            if self.left_tree:
                search_result = self.left_tree.search(data)
            else:
                search_result = False
        elif data > self.data:
            if self.right_tree:
                search_result = self.right_tree.search(data)
            else:
                search_result = False

        else:
            search_result = True  # is_find

        return search_result

    def preOrderTraversal(self, root):
        traversal_order = list()
        if root:
            traversal_order.append(root.data)
            traversal_order += self.preOrderTraversal(root.left_tree)
            traversal_order += self.preOrderTraversal(root.right_tree)

        return traversal_order

    def inOrderTraversal(self, root):
        traversal_order = list()
        if root:
            traversal_order += self.inOrderTraversal(root.left_tree)
            traversal_order.append(root.data)
            traversal_order += self.inOrderTraversal(root.right_tree)

        return traversal_order

    def postOrderTraversal(self, root):
        traversal_order = list()
        if root:
            traversal_order += self.postOrderTraversal(root.left_tree)
            traversal_order += self.postOrderTraversal(root.right_tree)
            traversal_order.append(root.data)

        return traversal_order


if __name__ == '__main__':
    insert_order = random.sample(range(1, 20), 7)
    print("insert order:", insert_order)

    bst = BinarySearchTree(insert_order[0])
    for data in insert_order[1:]:
        print('insert:', data)
        bst.insert(data)
    # bst = BinarySearchTree(5)
    # bst.insert(4)
    # bst.insert(3)
    # bst.insert(2)
    # bst.insert(1)
    # bst.insert(6)
    # bst.delete(3)

    print("Preorder: travalsal", bst.preOrderTraversal(bst))
    print("inorder: travalsal", bst.inOrderTraversal(bst))
    print("Postorder: travalsal", bst.postOrderTraversal(bst))

    print("from root: ", bst.data)
    trace_left_tree = bst.left_tree
    while trace_left_tree != None:
        print("find left tree: ", trace_left_tree.data)
        trace_left_tree = trace_left_tree.left_tree

    print("from right child node")
    trace_right_tree = bst.right_tree
    while trace_right_tree != None:
        print("find right tree: ", trace_right_tree.data)
        trace_right_tree = trace_right_tree.right_tree

    print("search 12:", bst.search(12))

    # test search
    print("test search start")
    targets_must_be_found = random.sample(insert_order, 5)
    for target in targets_must_be_found:
        # method 1
        is_find = bst.search(target)
        if is_find == False:
            print("something went wrong.")
        # method 2
        assert bst.search(target) == True, print(
            "something went wrong. by Assert")

    targets_must_not_be_found = [
        -1 * sample for sample in random.sample(insert_order, 5)]

    for fake_target in targets_must_not_be_found:
        assert bst.search(fake_target) == False, print(
            "something went wrong. by assert")
    print("test search done.")
