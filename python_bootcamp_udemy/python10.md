## 10일차 - 함수와 출력

##### 월별 일수
- 내 코드
```
# 윤년 여부 함수
 def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

# 윤년 유무 판단 함수
def days_in_month(year,month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if is_leap(year) and month ==2:
		return 29
	print(month_days[month-1])
  

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
```

    - 개선해야 할 점
        - month_days[month-1]에 대한 응용 공부가 필요!
        - 로직 계획에 대한 이해력 높여야한다.
        ==> 두개의 파라미터 설정 후 윤년인 경우에만 29일로 지정 (어떻게 코드를 짜야할지 떠오르지 않음)
        ==> list의 경우 0번 인덱스부터 시작이기에 -1 계산 필요!


## 계산기

- 코드

  ```
  from replit import clear
  from art import logo

  # 계산 함수 만들기
  def add(n1, n2):
    return n1 + n2

  def subtract(n1, n2):
    return n1 - n2

  def multiply(n1, n2):
    return n1 * n2

  def divide(n1, n2):
    return n1 / n2

  operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
  }

  # 계산기 함수 
  def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
      print(symbol)
    should_continue = True
   
   # 연속적으로 사칙연산 활용
    while should_continue:
      operation_symbol = input("Pick an operation: ")
      num2 = float(input("What's the next number?: "))
      calculation_function = operations[operation_symbol]
      answer = calculation_function(num1, num2)
      print(f"{num1} {operation_symbol} {num2} = {answer}")
  # 진행 여부에 따른 경우마다 결과물 제시
      if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
        num1 = answer
      else:
        should_continue = False
        clear()
        calculator()

  calculator()

  ```

  - 배운 점
    - 함수(calculator) 안에서 함수 (calculator)활용하기

