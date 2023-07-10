
# map 없이 숫자를 처리한 결과를 가지는 list
numberList = [i for i in range(1000)] # 0부터 999까지의 숫자를 가지고 리스트 생성
tempList = []
# 반복문을 사용한 변환 방식
for element in numberList:
    tempList.append(3 * element)
print(tempList)

def f(x):
    return 3 * x

# list의 모든 요소에 함수 f를 적용해서 반환한 결과를 temp에 대입
tempList = list(map(f, numberList)) # map 을 이용한 변환
print(tempList)

# f 함수가 1줄이므로 lamda로 표혆가능
tempList = list(map(lambda x : 3 * x, numberList))
print(tempList)

# map 을 이용해서 문자열을 대문자로 변환
def f(x):
    if len(x) > 2:
        return x[0:2] + x[2:].upper()
    return x

li = ["asdfasdf"]
temp = list(map(f,li))
print(temp)