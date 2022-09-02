## 1일차  

##### 밴드명 생성기

```
print("welcome to Band Name Generator")
# 도시이름 입력
city_name = input("What's name of the city you grew up in?\n")
# 강아지 이름 입력
pet_name = input("What's your pet's name?\n")
# 밴드이름 생성
print("Your band name could be " + city_name+' ' + pet_name)
```

![#day1](/day1.png)

## 2일차

##### BMI 계산기

```
# 키 입력
height = input("enter your height in m: ")

# 몸무게 입력
weight = input("enter your weight in kg: ")

# BMI 계산
BMI = float(weight)/(float(height))**2
print( " BMI 는 "+ str(int(BMI)) +"입니다.")
```

![day2_2](/day2_2.png)

* **반올림 round**
  print(round(8/3, 2))=2.67
  -> 2는 소수째 둘째짜리까지 나오게 반올림!
* **버림 //**
  print(8//3) = 2
  이때 type은 int( 버림을 하여서 float이 아닌)



##### 100살까지 남은 일,주,달 확인하기

```
# 나이 입력
age = input("What is your current age?")
# str-> int
int_age= int(age)
day =365*(100-int_age)
week=52*(100-int_age)
month=12*(100-int_age)
# f-string
message =f"너에게는 {day} 일, {week}주 ,{month}달이 남아있어 힘내!(기준 100살)"
print(message)
```

![day2_3](/day2_3.png)



##### 팁 계산기 프로젝트

- 내 코드

```
# 인사 멘트
print("Welcome to the tip calculator!")
# 총 비용
bills= input("What was the total bill? $")
# tip 비율
rate =input("WHat percentage tip would you like to give ? 10,12 or 15?")
# 총 인원 수
number=input("How many people to split the bill?")
# 한사람당 tip 비용계산
total= (float(bills) / int(number))*(1+(int(rate)/100))
# 둘째짜리까지 반올림
total_form = round(total,2)

print(f"Each perosn shold pay: $ {total_form}")
```



- 강사 코드

  ```
  print("Welcome to the tip calculator!")

  bills = float(input("What was the total bill? $"))

  rate = int(input("WHat percentage tip would you like to give ? 10,12 or 15?"))

  number = int(input("How many people to split the bill?"))
  total = (bills) / (number) * (1 + (rate / 100))
  total_form = "{:.2f}".format(total)

  print(f"Each perosn shold pay: $ {total_form}")
  ```

  ​

  - 놓쳤던 부분

    - 소수점 둘째짜리까지 나타내기 위해 round 를 활용함

      - 결과값이 33.60이라면 33.6으로 표시된다.(반올림 소수 몇번째짜리에 따른 문제가 아니다.)

        ==> **"{:.2f}".format(변수)**를 활용해야 33.60과 같이 둘째짜리까지 표시가능하다.

  - 아쉬운 부분

    - 변수를 지정할 떄 type까지 지정해주기.
      - 계산 시 덜 복잡해보이며 가독성이 더욱 좋아진다.

![day2](/day2.png)