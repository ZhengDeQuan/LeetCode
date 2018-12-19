# -*- coding:utf-8 -*-
import re
from collections import Iterable

class Node:
    def __init__(self , value = None , left = None , right = None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:

    def __init__(self , seq = ()):
        assert isinstance(seq,Iterable) #确保输入的参数是可叠代对象
        self.root = None

    def insert(self , *args):
        if not args:
            return
        if not self.root:
            self.root = Node(args[0])
            args = args[1:]
        for i in args:
            seed = self.root
            while True:
                if i > seed.value:
                    if not seed.right:
                        node = Node(i)
                        seed.right = node
                        break
                    else:
                        seed = seed.right
                else:
                    if not seed.left:
                        node = Node(i)
                        seed.left = node
                        break
                    else:
                        seed = seed.left

    def find(self, item , seed = None):
        node = seed or self.root
        parent = None
        while node:
            if item > node.value:
                parent , node = node , node.right
            elif item < node.value:
                parent , node = node, node.left
            else:
                return (node,parent)


    def minNode(self, seed=None):
        node = seed or self.root
        while node.left:
            node = node.left
        return node

    def maxNode(self, seed = None):
        node = seed or self.root
        while node.right:
            node = node.right
        return node

    def remove(self ,item):
        '''
        二叉树删除操作有点复杂。
        被删除节点没有子节点
        被删除节点有一个子节点
        被删除节点有两个子节点
        为方便描述，简称被删除节点为 A

        前两种比较简单，第一种只需要将 A 的父节点对应属性改为 None。第二种，需要将 A 的父节点与子节点关联。第三种就相对复杂一点，有两种方案，寻找 A 的右子树的最小值或左子树的最大值节点 B，根据 B 节点创建临时节点，删除节点 B，然后用临时节点替换 A 节点

        这里使用第一种方式，使用右子树最小值节点
        :param item:
        :return:
        '''
        Flag_Remove_Root = False
        result = self.find(item)
        if result is None:
            raise ValueError('item not in tree')
        del_node , del_node_parent = result
        if del_node_parent is None:
            #这种情况下删除的是根结点
            assert del_node == self.root
            if self.root.left is None:
                self.root = self.root.right
            elif self.root.right is None:
                self.root = self.root.left
            else:
                #找到右子树最小的节点
                pre = self.root.right
                if pre.left is None:
                    self.root.value = pre.value
                    self.root.right = pre.right
                    del pre
                    #以上这样处理，根结点左边的不用动
                else:
                    next_node = pre.left
                    while next_node.left is not None
                        pre = next_node
                        next_node = next_node.left
                    self.root.value = next_node.value
                    pre.left = next_node.right #不管next_node.right 是None还是有值都可以
                    del next_node
        else:
            if del_node.left is None:
                if del_node == del_node_parent.left:
                    del_node_parent.left = del_node.right
                else:
                    del_node_parent.right = del_node.right
                del del_node
            elif del_node.right is None:
                if del_node == del_node_parent.left:
                    del_node_parent.left = del_node.left
                else:
                    del_node_parent.right = del_node.left
            else:
                pre = del_node.right
                if pre.left is None:
                    del_node.value = pre.value
                    del_node.right = pre.right
                    del pre
                else :
                    next_node = pre.left
                    while next_node.left is not None:
                        pre = next_node
                        next_node = next_node.left
                    del_node.value = next_node.value
                    pre.left = next_node.right
                    del next_node







