#hw2 사칙연산 계산기 만들기(함수)

num=input("두 개의 숫자를 입력하세요 : ").split()
numm=list(map(int,num))

a=numm[0]
b=numm[1]
how=input("연산자를 입력하세요")

if how=="+":
    result=a+b
    print(f"덧셈결과 : {result}")
elif how=="-":
    if a>=b:
        result=a-b
    else:
        result="첫번째 입력한 수가 두번째 입력한 수보다 작습니다! 다시 입력해주세요!"

    print(f"뺄셈결과 : {result}") 
             
    
elif how=="*":
    result=a*b
    print(f"곱셈결과 : {result}")

elif how=="/":
    if b!=0:
        result=a/b
    else:
        result="0으로 나눌 수 없습니다! 다시 입력해주세요!"
    print(f"실수 나눗셈 결과 : {result}") 

elif how=="//":
    if b!=0:
        result=a//b
    else:
        result="0으로 나눌 수 없습니다! 다시 입력해주세요!"
    print(f"정수 나눗셈 결과 : {result}") 

elif how=="%":
    if b!=0:
        result=a%b
    else:
        result="0으로 나눌 수 없습니다! 다시 입력해주세요!"
    print(f"나머지 나눗셈 결과 : {result}") 

else:
    print("연산기호를 다시 입력해주세요!")
