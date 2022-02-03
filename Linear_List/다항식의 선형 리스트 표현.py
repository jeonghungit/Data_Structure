# 다항식을 선형 리스트로 표현
# P(x) = a + bx + cx^2 + dx^3 + ... + zx^n

# 다항식을 str로 표현
def printPoly(p_x):
    term = len(p_x) - 1
    polyStr = "P(x) = "

    for i in range(len(px)):
        coef = p_x[i]

        if coef >= 0:
            polyStr += "+"

        polyStr += str(coef) + "x^" + str(term) + " "
        term -= 1

    return polyStr


# str로 표현된 다항식을 계산
def calcPoly(xVal, p_x):
    retValue = 0
    term = len(p_x) - 1

    for i in range(len(px)):
        coef = p_x[i]
        retValue += coef * xValue ** term
        term -= 1

    return retValue


# 선형 리스트 전역 변수 선언
px = [7, -4, 0, 5]


# 메인 코드
if __name__ == "__main__":

    pStr = printPoly(px)
    print(pStr)

    xValue = int(input("X값 : "))

    pxValue = calcPoly(xValue, px)
    print(pxValue)
