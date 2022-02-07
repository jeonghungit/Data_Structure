# 양방향으로 링크가 연결되는 이중 연결 리스트를 만든다.
# head부터 차례대로 출력한 후 마지막 노드부터 거꾸로 다시 출력해보자.

class Node2():
    def __init__(self):
        self.plink = None
        self.data = None
        self.nlink = None


def printNodes(start):
    current = start
    if current.nlink == None:
        return
    print("정방향 : ", end=' ')
    print(current.data, end=' ')
    while current.nlink != None:
        current = current.nlink
        print(current.data, end=' ')
    print()
    print("역방향 : ", end=' ')
    print(current.data, end=' ')
    while current.plink != None:
        current = current.plink
        print(current.data, end=' ')


memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]


if __name__ == "__main__":

    node = Node2()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node2()
        node.data = data
        pre.nlink = node
        node.plink = pre
        memory.append(node)

    printNodes(head)




