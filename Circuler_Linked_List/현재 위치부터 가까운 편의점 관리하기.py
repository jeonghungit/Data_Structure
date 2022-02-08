# 현재 위치를 (0, 0)이라 가정하고, 편의점 위치(x, y)와 거리가 가까운 순서대로 원형 연결 리스트를 생성한다.
# 1. 편의점 10개를 A, B, C, ... 순서로 이름을 부여한다.
# 2. 편의점 위치 x와 y는 1부터 100까지 랜덤하게 좌표가 생성되도록 한다.
# 3. 현재 위치와 편의점 거리는 (x^2 + y^2)의 제곱근(sqrt)으로 계산한다.
# 4. 편의점 데이터 1개는 (편의점 이름, x좌표, y좌표)형식의 튜플로 구성한다.


import random
import math


class Node():
    def __init__(self):
        self.data = None
        self.link = None


def printStores(start):
    currnet = start
    if currnet == None:
        return

    while currnet.link != head:
        currnet = currnet.link
        x, y = currnet.data[1:]
        print(currnet.data[0], '편의점 거리 : ', math.sqrt(x*x + y*y))
    print()


def makeStoreList(store):
    global memory, head, current, pre

    node = Node()
    node.data = store
    memory.append(node)

    if head == None:
        head = node
        node.link = head
        return

    nodeX, nodeY = node.data[1:]
    nodeDist = math.sqrt(nodeX*nodeX + nodeY*nodeY)
    headX, headY = head.data[1:]
    headDist = math.sqrt(headX*headX + headY*headY)

    if headDist > nodeDist:
        node.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return

    current = head
    while current.link != head:
        pre = current
        current = current.link
        currX, currY = current.data[1:]
        currDist = math.sqrt(nodeX*nodeX + nodeY*nodeY)
        if currDist > nodeDist:
            pre.link = node
            node.link = current
            return

    current.link = node
    node.link = head


memory = []
head, current, pre = None, None, None


if __name__ == "__main__":

    storeArray = []
    storeName = 'A'
    for _ in range(10):
        store = (storeName, random.randint(1, 100), random.randint(1, 100))
        storeArray.append(store)
        storeName = chr(ord(storeName) + 1)

    for store in storeArray:
        makeStoreList(store)

    printStores(head)










