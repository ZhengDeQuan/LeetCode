# -*- coding:utf-8 -*-
# 如果是既有add_value,又有set_value, 那么应该需要两种标记，add_flg  和set_flg 而且逻辑上，set_的标记的优先级要高，即每次set的时候，要将add = 0
# 每次add的时候，需要set = - 1 , 如果set没有负值的话
# 每次push_down() if set > 0 then { add = 0 ; left.set = set , right.set = set , set =  - 1 ， }
# 或者更全面一点
'''
def push_down(self):
    if self.set_Enable is True:
        self.add = 0
        self.left.set = self.set
        self.right.set = self.set
        self.left.set_Enable = self.set_Enable
        self.right.set_Enable = self.set_Enable
        self.left.value = (self.left.r - self.right.l + 1 ) * self.set
        self.right.value = (self.right.r - self.right.l + 1) * self.set
        self.set_Enable = False
    else:
        self.left.add += self.add
        self.right.add += self.add
        self.left.value += (self.left.r - self.left.l + 1) * self.add
        self.right.value += (self.right.r - self.right.l + 1) * self.add
        self.add = 0

def push_up(self):
    self.value = self.left.value + self.right.vlaue
'''


class Tree(object):
    def __init__(self, l, r, value=0):
        self.l = l  # 对应真是数组的最左区间的index
        self.r = r  # 对应真实数组的最优区间的index
        self.value = value
        self.left = None
        self.right = None
        self.set = 0
        self.set_Enable = False
        self.add = 0
        if l < r:
            mid = l + ((r - l) >> 1)
            self.left = Tree(l, mid)
            self.right = Tree(mid + 1, r)

    def add_value(self, p, value):
        '''
        插点
        '''
        if p > self.r or p < self.l:
            return

        if self.l == self.r:
            self.value += value
            return

        self.push_down()
        mid = self.l + ((self.r - self.l) >> 1)

        if p <= mid:
            self.left.add_value(p, value)
        else:
            self.right.add_value(p, value)
        self.push_up()

    def add_value_interval(self, l, r, value):
        '''
        插线
        '''
        if l > self.right or r < self.left:
            return
        if l <= self.left <= self.right <= r:
            self.value += value * (self.r - self.l + 1)
            self.add += value
            return
        self.push_down()

        self.left.add_value_interval(l, r, value)
        self.right.add_value_interval(l, r, value)
        self.push_up()

    def push_up(self):
        self.value = self.left.value + self.right.value

    def push_down_1(self):
        if self.add == 0: return
        if self.left is not None:
            self.left.value += self.add * (self.left.r - self.left.l + 1)
            self.left.add += self.add
        if self.right is not None:
            self.right.value += self.add * (self.right.r - self.right.l + 1)
            self.right.add += self.add
        self.add = 0

    def push_down(self):
        if self.set_Enable is True:
            self.add = 0
            if self.left is not None:
                self.left.set = self.set
                self.left.set_Enable = self.set_Enable
                self.left.value = (self.left.r - self.right.l + 1) * self.set
            if self.right is not None:
                self.right.set = self.set
                self.right.set_Enable = self.set_Enable
                self.right.value = (self.right.r - self.right.l + 1) * self.set
            self.set_Enable = False
        elif self.add != 0:
            if self.left is not None:
                self.left.add += self.add
                self.left.value += (self.left.r - self.left.l + 1) * self.add
            if self.right is not None:
                self.right.add += self.add
                self.right.value += (self.right.r - self.right.l + 1) * self.add
            self.add = 0

    def query(self,p):
        '''
        问点
        '''
        if p > self.r or p < self.l:
            return None
        if self.l == self.r:
            return self.value
        self.push_down()
        mid = ((self.r - self.l) >> 1) + self.l
        if p<=mid:
            res = self.left.query(p)
        else:
            res = self.right.query(p)
        self.push_up()
        return res

    def query_interval(self, x, y):
        '''
        问线
        '''
        if x > self.r or y < self.l:
            return None

        if x <= self.l <= self.r <= y:
            return self.value

        self.push_down()
        mid = ((self.r - self.l) >> 1) + self.l
        if y <= mid:
            res = self.left.query_interval(x, y)
        elif x > mid:
            res =  self.right.query_interval(x, y)
        else:
            res = self.left.query(x, y) + self.right.query(x, y)
        self.push_up()
        return res

    def set_value(self , p , value):
        if self.l == self.r:
            self.value = value
            return
        self.push_down()
        mid = ((self.r - self.l) >> 1) + self.l
        if p<=mid:
            self.left.set_value(p,value)
        else:
            self.right.set_value(p,value)
        self.push_up()

    def set_value_interval(self , x, y, value):
        if (x > self.r) or (y < self.l) :
            return
        if (x <= self.l  <= self.r <= y):
            self.value = value * (self.r - self.l + 1)
            self.set_Enable = True
            self.set = True
            return
        self.push_down()
        self.left.set_value_interval(x, y, value)
        self.right.set_value_interval(x, y, value)
        self.push_up()



def main():
    N = 1024
    import time
    old = time.time()
    tree = Tree(0, N)
    for i in range(N + 1):
        # print i
        tree.set_value(i, 1)
    print(tree.query(30, 60))
    print(time.time() - old)

if __name__ == "__main__":
    main()




