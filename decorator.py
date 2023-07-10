from datetime import datetime

"""
def deco(func):
    print("common")
    func()

def getTime():
    present = datetime.now()
    return present

# 이제 business 함수를 실행하면 대신 deco 를 실행
# deco 함수를 실행하면서 func 부분에 기존의 business 함수를 대입함
# 그 결과 common 과 business 둘 다 출력함
# business 함수를 수정하지 않고 common 이나 logging 에 변화를 줄 수 있음
@deco # decorator 부분
def business():
    print("business")

business()

"""

# 함수를 호출할 때 마다 실행에 걸린 시간, 인수, 리턴 값을 출력하는 decorator 를 생성

def timeDiff(func):
    # decorator 가 적용된 함수가 호출되면 실제로 수행되는 함수
    def clock(*args):
        beforeTime = getTime() # 현재 시간

        # 업무 로직 함수 호출
        func(*args)
        afterTime = getTime()
        timeDiffer = afterTime - beforeTime # 로직 수행에 걸린 시간
        print("매개변수 : " + str(*args)) # 매개변수 확인
        print(timeDiffer)
        return timeDiffer
    return clock

def getTime():
    present = datetime.now()
    return present


@timeDiff # decorator 부분
def absNumber(numberRange):
    absSum = 0

    for i in range(2, numberRange + 1):
        arrSum = 1 
        for j in range(2, i // 2 + 1): # 나머지가 0인 숫자가 약수
            if i % j == 0:
                arrSum += j
        if arrSum == i: # 완전수 판별
            absSum += 1
    return absSum

absNumber(2000)