## 5일차

##### 학생 평균 키(for 문 활용)

- 제시

  ```
  # 🚨 Don't change the code below 👇
  student_heights = input("Input a list of student heights ").split()
  for n in range(0, len(student_heights)):
      student_heights[n] = int(student_heights[n])
  # 🚨 Don't change the code above 👆
  ```

  ​

- 내 코드

  ```
  student_heights_sum = sum(student_heights)
  student_heights_average = (student_heights_sum) / len(student_heights)
  average_student = round(student_heights_average)
  print(average_student)
  ```

  ​

- 강사 코드

  ```
  total_height = 0
  for height in student_heights:
  	total_height += height

  number_of_students=0
  for studnet in student_heights:
  	number_of_students +=1
  	
  average_height =round(total_height/ number_of_studensts)
  print(average_height)
  ```

  - 개선해야 할 점
    - sum(),len() 함수 활용도 좋지만 for 반복문을 통해서도 구현 가능함.

##### 높은 점수 구하기(for문 활용)

- 제시

  ```
  # 🚨 Don't change the code below 👇
  student_scores = input("Input a list of student scores ").split()
  for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
  print(student_scores)
  # 🚨 Don't change the code above 👆
  ```

  ​

- 내 코드

  ```
  stduent_scores=[71,55,69,81,47,88]

  for score in students_scores:
    score[n+1] - score[n] >
    
  # 작성 못함
  ```

  ​

- 강사 코드

  ```
  highest_score=0
  for score in student_scores:
    if score > highest_score:
      highest_score=score
  print(f"가장 큰 숫자는 {score}입니다.")
  ```

  * 개선할 부분
    * if문 활용 생각은 있었으나 구현하는데 어려움이 있었음
    * **for문에 대한 이해 복습필요**



##### 비밀번호 생성기

- 제시

  ```
  import random
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  print("Welcome to the PyPassword Generator!")
  nr_letters= int(input("How many letters would you like in your password?\n")) 
  nr_symbols = int(input(f"How many symbols would you like?\n"))
  nr_numbers = int(input(f"How many numbers would you like?\n"))

  ```

  ​

- 내 코드

  ```
  S = random.sample(symbols,nr_symbols)
  L = random.sample(letters,nr_letters )
  N = random.sample(numbers,nr_numbers)
  password= L+S+N
  password_join=''
  for p in password:
    password_join += p
  print(f'새로운 비밀번호는 {password_join}입니다.')
  ```

  ​

- 강사 코드(Easy mode / 문자, 특수부호, 번호 순)

  ```
  password = ""

  for char in range(1, nr_letters + 1):
    password += random.choice(letters)

  for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)

  for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

  print(password)
  ```

  ​

- 강사코드(Hard mode / 문자, 특수부호, 번호 랜덤)

  ```
  password_list = []

  for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

  for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

  for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

  print(password_list)
  random.shuffle(password_list)
  print(password_list)

  password = ""
  for char in password_list:
    password += char

  print(f"Your password is: {password}")
  ```

  - 개선해야 할 점

    - (Easy mode)각각 for문을 통해 얻은 결과값을 password=""에 더하여 도출

      ==> **for문  활용에 대한 응용력 부족**

    - (Hard mode)**리스트의 내용을 문자열로 합쳐보여줄 때**

      ```
      password = ""
      for char in password_list:
        password += char
      ```

      ==> join 활용보다 for문 활용이 간결

    ​