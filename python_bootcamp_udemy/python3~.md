## 3일차

##### 홀짝 알려주기

```
if number % 2 ==0:
  print("This is an even number")
else:
  print("This is an odd number")
```



##### 윤년 구하기

```
if year % 4 == 0:
	if year % 100 == 0:
		if year % 400 == 0:
			print('윤년이다.')
		else:
			print('윤년이 아니다.')
	else:
		print('윤년이다.')
else:
	print("윤년이 아니다.")
```



##### 피자 주문하기

- 내 코드

```
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

if size == 'S':
    bill = 15

if size == 'M':
    bill = 20
   
if size == 'L':
    bill = 25
    
# 오류    
# if add_pepperoni == "Y":
#   if size == "S":
#       bill = bill + 2
#   if size == "M" and size == "L":
#       bill = bill + 3
# else :
#   bill = bill

if add_pepperoni == "Y" and size == "S":
    bill = bill + 2
if add_pepperoni == "Y" and size == "M":
    bill = bill + 3
if add_pepperoni == "Y" and size == "L":
    bill = bill + 3

if extra_cheese == "Y":
    bill = bill + 1
    print(f'최종 {bill}달러입니다.')
else:
    print(f'최종 {bill}달러입니다.')
```

- 강사 코드

  ```
  print("Welcome to Python Pizza Deliveries!")
  size = input("What size pizza do you want? S, M, or L ")
  add_pepperoni = input("Do you want pepperoni? Y or N ")
  extra_cheese = input("Do you want extra cheese? Y or N ")

  bill = 0

  if size == 'S':
      bill += 15

  if size == 'M':
      bill += 20
     
  if size == 'L':
      bill += 25
      
  if add_pepperoni == "Y":
  	if size == "S"
  		bill +=2
      else:
      	bill +=3
      	
  if extra_cheese == "Y":
      bill += 1
  print(f'최종 {bill}달러입니다.')
  ```



![pizza](./pizza.png)

- 놓쳤던 부분
  - print를 마지막 if문에 넣어주어서  add_pepperoni에 대한 처리가 되지 않아 코드를 통한 계산오류


- 아쉬운 부분
  - bill = bill +3 과 같은 표현을 bill +=3으로 가독성 좋게 표현할 것