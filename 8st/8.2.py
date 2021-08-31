#8주차 이론실습-2
#생성자,메소드
#class내부에 있는 함수 -> 메소드
class student:
    def __init__(self,name,korean,math,english,science): #생성자
        self.name= name 
        self.koean=korean
        self.math =math
        self.english=english
        self.science=science
    def get_sum(self):
        return self.koean +self.math + self.english +self.science #내부변수를 이용하고 싶으면 꼭 self.~

    def average(self):
        return "{:2f}".format(self.get_sum() / 4)

   # print(student.get_sum()) #그냥 get_sum을 쓰지는 못한다!!!


students=[
    student("송강호",98,100,100,100),
    student("아이유",100,91,95,97),
    student("송중기",100,97,92,94),
    student("김태리",97,93,92,97),
    student("송강",93,79,93,97),
    ]


for student in students:
    print(f"{student.name} 총점: {student.get_sum()}  평균: {student.average()}")