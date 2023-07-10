# 조건에 맞는 데이터만 리턴하는 filter 함수

arr = ["123", "1234", None, "12","31412" "1", ""]

# 결측치 탐색
print(None in arr) # None 이 있으면 True 반환

# None 을 지우기
def deleteNone(x):
    return x != None

arr = list(filter(deleteNone, arr))
# lamda 로 함수를 대체
#arr = list(filter(lambda x : x != None, arr)) lamda 로 함수를 대체
print(arr) # "" 는 None 이 아니기 때문에 지워지지 않음


# 데이터가 collection 에 포함되어 있는지 확인하기 : in(반대는 not in)
# 3을 포함하는 데이터만 리턴
def f(x):
    return "3" in x

needData = "3"

arr = list(filter(f, arr))
# lambda 로 함수를 대체
# needData 에 포함되는 데이터를 가진 데이터만 추출
arr = list(filter(lambda x : needData in x , arr)) 
print(arr)

print("가" <= "나") # True

arr = ["가", "김씨","박"]
# arr 에서 이름 성씨가 '가' 와 '나' 사이인 사람만 추출
# 문자열은 '"가" < "나"' 와 같이 비교가 가능함
arr = list(filter(lambda x : x[0] >= "가" and x[0] <= "나", arr))
print(arr)
