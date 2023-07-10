def outer():
    outerData = "외부 데이터"

    def inner():
        innerData = "내부 데이터"
        # inner 가 아니라 outer 의 데이터를 내부에서 사용.
        nonlocal outerData
        print(outerData)
        # local 데이터를 만드는 것이 아니라 외부의 데이터를 수정.
        outerData = "내부에서 변경"
        print(outerData)
        print(innerData)

    inner()
    print(outerData) # 내부의 변경이 반영됨

outer() 