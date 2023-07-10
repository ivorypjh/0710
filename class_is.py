class Study:
    class_data = "클래스 속성"

student1 = Study()
student2 = Study()
# student1 의 데이터를 대입
# student1 이 참조하고 있는 데이터의 참조를 student3 가 참조함
student3 = student1

# 2개의 인스턴스가 같은지 확인
# 둘 다 False
# 둘 다 인스턴스 생성이 되어서 별도의 메모리를 받음
print(student1 == student2) # 내부의 데이터가 같은지 확인
print(student1 is student2) # id 가 같은지 확인
# 새로 인스턴스를 생성한게 아니기에 같음
print(student1 == student3) # True
print(student1 is student3) # True