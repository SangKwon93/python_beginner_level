## 13일차 - Debug

##### 홀짝 알려주기

- 기본 코드

  ```
  number = int(input("Which number do you want to check?"))

  if number % 2 = 0:
    print("This is an even number.")
  else:
    print("This is an odd number.")
  ```

  ​

- Debug 

  - 부등호 = 이 아니라**==**



##### 윤년 맞추기

- 기본 코드

  ```
  year = input("Which year do you want to check?")

  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print("Leap year.")
      else:
        print("Not leap year.")
    else:
      print("Leap year.")
  else:
    print("Not leap year.")
  ```

  ​

- Debug

  - input 함수는 문자열로 변환하여 반환한다.

  - year = **int**(input("Which year do you want to check?")) 로 해야 오류 해결

    ​

##### 피즈 버즈

- 기본 코드

  ```
  for number in range(1, 101):
    # case1
    if number % 3 == 0 or number % 5 == 0:
      print("FizzBuzz")
    # case2
    if number % 3 == 0:
      print("Fizz")
    # case3
    if number % 5 == 0:
      print("Buzz")
    # case4
    else:
      print([number])
  ```



- Debug
  - if로 모두 하게되면 각 if에 해당되는 else가 필요하며 각각의 조건이 되어버린다.
  - **if를 elif**로 변경하여 case1~4중에 하나로 택하게 코드를 수정