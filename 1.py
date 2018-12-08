import os
import sys

import queue as Q
# que = Q.PriorityQueue()
# que.put(10)
# que.put(1)
# que.put(5)
# while not que.empty():
#     print(que.get())
#
# que = Q.PriorityQueue()
# que.put((10,'ten'))
# que.put((1,'one'))
# que.put((10/2,'five'))
# while not que.empty():
#     print(que.get())

class Skill(object):
    def __init__(self,priority,description):
        self.priority = priority
        self.description = description
    #下面两个方法重写一个就可以了
    def __lt__(self,other):#operator <
        return self.priority > other.priority

    def __str__(self):
        return '(' + str(self.priority)+',\'' + self.description + '\')'


class ToBeCmp(object):
    def __init__(self , word , hot):
        self.word = word
        self.hot = hot

    def __lt__(self , other):
        return self.hot > other.hot

    def __str__(self):
        return str([self.hot , self.word])
#
# que = Q.PriorityQueue()
# skill5 = Skill(5,'proficient')
# skill6 = Skill(6,'proficient6')
# que.put(skill6)
# que.put(Skill(5,'proficient'))
# que.put(Skill(10,'expert'))
# que.put(Skill(1,'novice'))
# while not que.empty():
#     print(que.get())


if __name__ == "__main__":
    MyDict = dict()
    que = Q.PriorityQueue()
    sys.stdin = open("input.txt","r")
    n = input()
    n = int(n)
    print("n = ",n)
    while n>0:
        n -= 1
        line = input()
        print("line = ",line)
        word , hot = line.split()
        hot = int(hot)
        sorted_word = sorted(word)
        sorted_word = ''.join(sorted_word)
        print("word = ",word)
        print("sorted_word = ",word)
        if sorted_word not in MyDict:
            MyDict[sorted_word] = []
            MyDict[sorted_word].append(ToBeCmp(word,hot))
        else:
            MyDict[sorted_word].append(ToBeCmp(word,hot))

    m = input()
    m = int(m)
    print("m = ",m)
    while m > 0:
        m -= 1
        query = input()
        print("query = ",query)
        query = sorted(query)
        query = ''.join(query)
        if query in MyDict:
            res = MyDict[query]
        else:
            res = []

        while que.empty() is False:
            que.get()
        for item in res:
            que.put(item)

        while que.empty() is False:
            ans = que.get()
            print("ans = ",ans.hot,ans.word)

            # hot,word = ans[1:-1].split(',')
            # hot = int(hot)
            # word = word.strip()
            # print("hot = ",hot)
            # print("word = ",word)

