# 튜플로 이루어진 리스트에 카톡 횟수 기준으로 정렬되게 새로운 친구를 삽입한다.

# 입력받은 카톡횟수(k_count)와 튜플 내 카톡횟수(pair[1])를 비교하여 입력값의 인덱스를 찾는다.
def find_and_insert_data(friend, k_count):
    findPOS = -1

    for i in range(len(katok)):
        pair = katok[i]

        if k_count >= pair[1]:
            findPOS = i
            break

    if findPOS == -1:
        findPOS = len(katok)

    insert_data(findPOS, (friend, k_count))


# 새로운 입력값을 기존의 선형 리스트에 삽입하는 과정.
def insert_data(position, friend):
    if position < 0 or position > len(katok):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return

    katok.append(None)
    kLen = len(katok)

    for i in range(kLen -1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None

    katok[position] = friend


# 기존의 튜플로 이루어진 선형 리스트
katok = [('다현', 200), ('정연', 150), ('쯔위', 90), ('사나', 30), ('지효', 15)]


if __name__ == "__main__":

    data = input("추가할 친구 : ")
    count = int(input("카톡 횟수 : "))
    find_and_insert_data(data, count)
    print(katok)