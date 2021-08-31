#hw3 숫자의 약수 구하기 & 숫자 분류하기

num = int(input("숫자를 입력하세요 : "))

list_1=[]
for i in range(1,num):
   if num%i==0 :
      list_1.append(i)
print(f"{num}의 약수 :{list_1[0:]}")
