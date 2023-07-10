class Study:
    # 클래스의 속성
    studyData = "클래스의 속성"
    # 인스턴스가 있어야만 호출되는 메서드

# 인스턴스 생성
student = Study()
# 둘의 결과는 동일
print(Study.studyData) # 클래스 이름을 이용해서 클래스 속성에 접근
print(student.studyData) # 인스턴스 이름을 이용해서 클래스 속성에 접근
Study.studyData = "클래스 속성 수정됨" # 클래스 이름을 사용해서 속성 수정
print(Study.studyData) # 클래스 속성 수정됨
print(student.studyData) # 클래스 속성 수정됨
# studyData 는 클래스에 있는 데이터이지 인스턴스에 있는게 아님
# 대입을 하는 문장이므로 인스턴스에 studyData 를 생성함
# 클래스는 기존에 가지고 있던 studyData 데이터를 출력
student.studyData = "인스턴스를 사용해서 속성 수정"
print(Study.studyData) # 클래스 속성 수정됨
print(student.studyData) # 인스턴스를 사용해서 속성 수정

