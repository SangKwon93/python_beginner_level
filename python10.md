## 10일차 - 함수와 출력

##### 월별 일수
- 코드
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

    - 개선해야 할 점
        - month_days[month-1]에 대한 응용 공부가 필요!
        - 로직 계획에 대한 이해력 높여야한다.
        ==> 두개의 파라미터 설정 후 윤년인 경우에만 29일로 지정 (어떻게 코드를 짜야할지 떠오르지 않음)
        ==> list의 경우 0번 인덱스부터 시작이기에 -1 계산 필요!