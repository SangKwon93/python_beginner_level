
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


        
## 강사 코드(암호/복호화)
def encrypt(plain_text,shift_amount):
    cipher_text=""
    for letter in plain_text:
        position=alphabet.index(letter)
        new_position= position+shift_amount
        cipher_text += alphabet[new_position]
    print(f'암호화한 내용은 {cipher_text}입니다.')


def decrypt(cipher_text,shift_amount):
    plain_text=''
    for letter in cipher_text:
        position=alphabet.index(letter)
        new_position= position-shift_amount
        plain_text += alphabet[new_position]
    print(f'복호화한 내용은 {plain_text}입니다.')
    
if direction == 'encode':
    encrypt(text,shift)
elif direction == 'decode':
    decrypt(text,shift)


## Final_code
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


       
