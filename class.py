# 메서드의 생성과 호출, 인스턴스, 속성

class Study:
    # 인스턴스가 있어야만 호출되는 메서드
    def display(self):
        print("인스턴스 생성됨")

    def setName(self, name):
        # self.name 은 인스턴스의 속성으로 만들어짐.
        # name 만 사용했다면 지역 변수가 됨.
        self.name = name 

# 인스턴스 생성하기
# student 라는 이름을 가지는 인스턴스 생성, 괄호 필요
# student 는 인스턴스가 아님. 인스턴스는 오른쪽의 Study()
# 나중에 다시 활용하기 위해 이름을 붙인 것.
student = Study() # student 는 인스턴스가 아님.

student.setName("박") # 가지고 있던 속성에 대입
print(student.name)
student.grade = "A"  # 없던 속성을 동적으로 생성
print(student.grade)

Study().display() # Study() 가 인스턴스이기에 이런 방식으로 호출 가능

# 메서드 호출 - 인스턴스를 활용한 bound 호출 방식
student.display()
# 메서드 호출 - 파이썬에서 제공하는 unbound 호출 방식
Study.display(student)