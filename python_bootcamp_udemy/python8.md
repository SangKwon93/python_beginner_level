## 8일차 - 함수 매개변수

## 소수 확인기

- 내 코드

  ```
  def prime_checker(number):
    if number == 2 or number ==3 :
      print(f"{number}은 소수입니다.")
    else:
          if number % 2 !=0:
              if number % 3 !=0:
                  print(f"{number}은 소수입니다.")
              else:
                  print(f"{number}은 소수가 아닙니다.")
          
  			
  n = int(input("Check this number: "))
  prime_checker(number=n)
  ```

  ==> 2와 3의 배수인 6의 배수의 경우 오류발생

  ==> 소수의 원리에 따라 코드 작성해야하나 다른 방식으로 접근한 것이 잘못됨

  ==> 소수란 1과 내 자신을 제외한 숫자로 나누어야하며 나머지가 0이 아니어야한다.

  ​

- 강사 코드

  ```
  def prime_checker(number):
      is_prime=True
      for i in range(2,number):
          if number % i ==0:
              is_prime=False
      if is_prime == True:
          print(f"{number}은 소수이다.")
      else:
          print(f"{number}은 소수가 아닙니다.")
          
              
  n = int(input("Check this number: "))
  prime_checker(number=n)
  ```

  - 개선해야 할 점
    - 로직을 계획할 때 특징을 코드로 옮기는데 미흡
    - for문의 활용이 미흡



## 암호화/복호화

- 내 코드

  ```
  def encrypt(plain_text,shift_amount):
  	
      position=len(plain_text)
      for char in range(position):
          change_text=""
          #plain_text[char] #hello[0]=h
          num = int(alphabet.index(plain_text[char]))+shift_amount
          change_text +=alphabet[num]
      print(f'암호화한 내용은 {change_text}입니다.')
          
  encrypt(plain_text= text,shift_amount=shift)
  ```

  ​

- 강사 코드(암호화)

  ```
  def encrypt(plain_text,shift_amount):
      cipher_text=""
      for letter in plain_text:
          position=alphabet.index(letter)
          new_position= position+shift_amount
          cipher_text += alphabet[new_position]
      print(f'암호화한 내용은 {cipher_text}입니다.')
  ```

  ​

- 강사코드(복호화)

  ```
  def decrypt(cipher_text,shift_amount):
      plain_text=''
      for letter in cipher_text:
          position=alphabet.index(letter)
          new_position= position-shift_amount
          plain_text += alphabet[new_position]
      print(f'복호화한 내용은 {plain_text}입니다.')
  ```

  ​

- 코드 합치기

  ```
  # 메시지, 이동수, 암호,복호화 함수 합치기
  def caesar(start_text,shift_amount,cipher_direction):
      end_text=""
      if cipher_direction == "decode":
          shift_amount*=-1
      for char in start_text:
          if char in alphabet:
              position=alphabet.index(char)
              new_position=position + shift_amount
              end_text+= alphabet[new_position]
          else:
              end_text+=char
      print(f" {direction}된 결과는 {end_text}이다.")
          
  from art import logo
  print(logo)

  # flag 변수
  should_end=False
  while not should_end:
      direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
      text = input("Type your message:\n").lower()
      shift = int(input("Type the shift number:\n"))
      shift = shift % 26
      caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
      restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
      if restart == "no":
          should_end = True
          print("종료")
  ```

  - 개선 해야 할 점

    ```
     position=len(plain_text)
        for char in range(position):
            change_text=""
            #plain_text[char] #hello[0]=h
            num = int(alphabet.index(plain_text[char]))+shift_amount
            change_text +=alphabet[num]
    ```

    ```
    cipher_text=""
        for letter in plain_text:
            position=alphabet.index(letter)
            new_position= position+shift_amount
            cipher_text += alphabet[new_position]
    ```

    ​

    - change_text=""와 같이 빈 공백 문자열을 통해 각 철자 합치기

    - range 보다는 순서만 설정하면 가능

      ==> **추후 다시 학습 필요**