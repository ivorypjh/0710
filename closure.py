def outer():
    outerData = 1

    # 자신을 감싸는 외부 함수의 데이터를 수정하는 함수
    def inner():
        nonlocal outerData
        outerData = outerData + 1
        print(outerData)
    # 함수 내부의 데이터를 수정하는 함수를 리턴하는 함수를 closure 라고 함.
    return inner

result = outer()
result()
result()
# outerData = outerData + 1 
# 함수 내부에서 만들어진 데이터이므로 사용 불가능