# 1~45 숫자 6개를 뽑는 추첨 프로그램을 코딩한다.

import random

# 빈 노드 객체 생성
class Node():
    def __init__(self):
        self.data = None
        self.link = None


# current 노드의 링크를 따라가며 링크가 없을 때까지 currnet.data를 출력한다.
def printNode(start):
    current = start
    if current == None:
        return
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()


# head, current, pre가 가리키는 노드와 새로운 노드를 비교하며 적절한 위치를 찾아 링크한다.
def makeLottoList(num):
    global memory, head, current, pre

    node = Node()
    node.data = num
    memory.append(node)

    if head == None:
        head = node
        return

    if head.data > num:
        node.link = head
        head = node
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data > num:
            pre.link = node
            node.link = current
            return

    current.link = node


def findNumber(num):
    global memory, head, current, pre

    if head == None:
        return False
    current = head
    if current.data == num:
        current = current.link
        if current.data == num:
            return True
        return False


memory = []
head, current, pre = None, None, None


if __name__ == "__main__":

    lottoConunt = 0
    while True:
        lotto = random.randint(1, 45)
        if findNumber(lotto):
            continue
        lottoConunt += 1
        makeLottoList(lotto)
        if lottoConunt >= 6:
            break

    printNode(head)





