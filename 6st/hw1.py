#hw1 기계와 다른숫자를 가지고 있는 카드게임
jay=input("Jay가 선택한 카드(1~9에서 5장):").split()
jay2=list(map(int,jay))

emily=input("Emily가 선택한 카드(1~9에서 5장):").split()
emily2=list(map(int,emily))

from array import array
import random
com=random.sample(range(1,10),3)
com1=com[0]
com2=com[1]
com3=com[2]
print(f"기계가 선택한 카드(1~9에서 3장) : {com1} {com2} {com3} ")



if len(jay2)==5 & len(emily)==5:

    a=set(jay2)
    b=set(emily2)
    c=set(com)
    d=a-c
    e=b-c

    num_j=len(d)
    num_e=len(e)

    if num_j>num_e :
        print(f"Emily대 Jay는 {num_j}:{num_e}로 Jay 승 !")
    elif num_j<num_e :
        print(f"Emily대 Jay는 {num_j}:{num_e}로 Emily 승 !")
    else :
        print("무승부입니다!")
else :
    print("카드 5장을 다시 선택하세요.")