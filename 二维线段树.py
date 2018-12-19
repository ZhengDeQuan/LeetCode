# -*- coding:utf-8 -*-
# 二维线段树

def get_mid(l , r):
    return l + ((r-l) >> 1)

class Tree(object):
    def __init__(self,x1,x2,y1,y2,value=0):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.value = value
        self.set = 0
        self.setEnable = False
        self.add = 0
        if l < r :
            midx = x1 + ((x2 - x1) >> 1)
            midy = y1 + ((y2 - y1) >> 1)
            self.x1y1 = Tree(x1,midx,y1,midy)
            self.x1y2 = Tree(x1,midx,midy+1,y2)
            self.x2y1 = Tree(midx+1,x2,y1,midy)
            self.x2y2 = Tree(midx+1,x2,midy+1,y2)

    def get_interval(self):
        return (self.y2 - self.y1 + 1) * (self.x2 - self.x1 + 1)

    def push_down(self):
        if self.setEnable is True:
            self.add = 0
            if self.x1y1 is not None:
                self.x1y1.set = self.set
                self.x1y1.setEnable = self.setEnable
                self.x1y1.value = self.x1y1.get_interval() * self.set
            if self.x1y2 is not None:
                self.x1y2.set = self.set
                self.x1y2.setEnable = self.setEnable
                self.x1y2.value = self.x1y2.get_interval() * self.set
            if self.x2y1 is not None:
                self.x2y1.set = self.set
                self.x2y1.setEnable = self.setEnable
                self.x2y1.value = self.x2y1.get_interval() * self.set
            if self.x2y2 is not None:
                self.x2y2.set = self.set
                self.x2y2.setEnable = self.setEnable
                self.x2y2.value = self.x2y2.get_interval() * self.set
            self.setEnable = False

        elif self.add != 0:
            if self.x1y1 is not None:
                self.x1y1.add = self.add

                self.x1y1.value = self.x1y1.get_interval() * self.add
            if self.x1y2 is not None:
                self.x1y2.add = self.add

                self.x1y2.value = self.x1y2.get_interval() * self.add
            if self.x2y1 is not None:
                self.x2y1.add = self.add

                self.x2y1.value = self.x2y1.get_interval() * self.add
            if self.x2y2 is not None:
                self.x2y2.add = self.add

                self.x2y2.value = self.x2y2.get_interval() * self.add
            self.add = 0

    def push_up(self):
        self.value = self.x1y1.value + self.x1y2.value + self.x2y1.value + self.x2y2.value

    def add_value(self,posx,posy,value):
        '''
        插点
        '''
        if posx < self.x1 or posx > self.x2 or posy < self.y1 or posy > self.y2:
            return

        if self.x1 == self.x2 and self.y1 == self.y2:
            self.value += value
            return

        self.push_down()
        midx = get_mid(self.x1,self.x2)
        midy = get_mid(self.y1,self.y2)

        if posx <= midx and posy <= midy:
            self.x1y1.add_value(posx,posy,value)
        elif posx <= midx and posy > midy:
            self.x1y2.add_value(posx,posy,value)
        elif posx > midx and posy <= midy:
            self.x2y1.add_value(posx,posy,value)
        elif posx > midx and posy > midy:
            self.x2y2.add_value(posx,posy,value)
        self.push_up()

    def add_value_interval(self,x1,x2,y1,y2,value):
        '''
        插线
        '''
        if x1 > self.x2 or x2 < self.x1 or y1 > self.y2 or y2 < self.y1:
            return
        if x1 <= self.x1<= self.x2<=x2 and y1<=self.y1<=self.y2<=y2:
            self.value += value * self.get_interval()
            self.add += value
            return
        self.push_down()
        self.x1y1.add_value_interval(x1,x2,y1,y2,value)
        self.x1y2.add_value_interval(x1,x2,y1,y2,value)
        self.x2y1.add_value_interval(x1,x2,y1,y2,value)
        self.x2y2.add_value_interval(x1,x2,y1,y2,value)
        self.push_up()

    def set_value(self,posx,posy , value):
        if self.x1 == self.x2 and self.y1 == self.y2:
            self.value = value
            return
        self.push_down()
        midx = get_mid(self.x1,self.x2)
        midy = get_mid(self.y1,self.y2)

        if posx <= midx and posy <= midy:
            self.x1y1.set_value(posx,posy,value)
        elif posx <= midx and posy > midy:
            self.x1y2.set_value(posx,posy,value)
        elif posx > midx and posy <= midy:
            self.x2y1.set_value(posx,posy,value)
        elif posx > midx and posy > midy:
            self.x2y2.set_value(posx,posy,value)
        self.push_up()

    def set_value_interval(self, x1, x2, y1, y2,value):
        if x1 > self.x2 or x1 < self.x1 or y1 < self.y1 or y2 > self.y2:
            return
        if x1 <= self.x1 <= self.x2 <= x2 and y1 <= self.y1 <= self.y2 <= y2:
            self.value = value * self.get_interval()
            self.setEnable=True
            self.set = value
            return
        self.push_down()
        self.x1y1.add_value_interval(x1, x2, y1, y2, value)
        self.x1y2.add_value_interval(x1, x2, y1, y2, value)
        self.x2y1.add_value_interval(x1, x2, y1, y2, value)
        self.x2y2.add_value_interval(x1, x2, y1, y2, value)
        self.push_up()

    def query(self,posx,posy):
        if posx < self.x1 or posx > self.x2 or posy < self.y1 or posy > self.y2:
            return None
        if self.x1 == self.x2 and self.y1 == self.y2:
            return self.value
        self.push_down()
        midx = get_mid(self.x1,self.x2)
        midy = get_mid(self.y1,self.y2)
        res = 0
        if posx <= midx and posy <= midy:
            res += self.x1y1.set_value(posx,posy)
        elif posx <= midx and posy > midy:
            res += self.x1y2.set_value(posx,posy)
        elif posx > midx and posy <= midy:
            res += self.x2y1.set_value(posx,posy)
        elif posx > midx and posy > midy:
            res += self.x2y2.set_value(posx,posy)
        self.push_up()
        return res

    def query_interval(self,x1,x2,y1,y2):
        if x1 > self.x2 or x2 < self.x1 or y1 > self.y2 or y2 < self.y1:
            return None
        if x1 <= self.x1 <= self.x2 <= x2 and y1 <= self.y1 <= self.y2 <= y2:
            return self.value
        self.push_down()
        res = 0
        res += self.x1y1.query_interval(x1,x2,y1,y2)
        res += self.x1y2.query_interval(x1,x2,y1,y2)
        res += self.x2y1.query_interval(x1,x2,y1,y2)
        res += self.x2y2.query_interval(x1,x2,y1,y2)
        self.push_up()
        return res

if __name__ == "__main__":
    N = 1024
    tree = Tree(0,N,0,N)
    for i in range(N + 1)
        tree.set_value(0,i,1)
    print(tree.query(30, 60))










