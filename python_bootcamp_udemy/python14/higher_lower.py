from game_data import data
import random
from higher_lower_logo import logo,vs
from replit import clear

# 구현할 내용
# Compare A : Neymar, a Footballer, from Brasil.

# Against B : ~~~~

# Who has more followers? Type 'A' or 'B'

# Wrong : print("Sorry, that's wrong. Final score:0")

# Right
# You are right! Current score:1

# Compare A : Neymar, a Footballer, from Brasil.
# Against B : ~~~~
# Who has more followers? Type 'A' or 'B'

# Wrong : print("Sorry, that's wrong. Final score:0")

def random_info():
    return random.choice(data)

#print(random_info())


# input 작성
def get_info(info):
    name=info["name"]
    description=info["description"]
    country=info["country"]
    #print(f'Compare A : {name}, a {description}, from {country}.')
    #print(f'Against B : {name}, a {description}, from {country}.')
    return f' {name}, a {description}, from {country}.'

# 비교 함수 작성
def num_check(guess,a_followers, b_followers):
    if a_followers > b_followers:
        return guess=="a"
    else:
        return guess=="b"


# 게임 작동 함수
# 정답일 때 While문
# 오답일 때 종료
def get_start():
    print(logo)
    # score=0
    should_continue = True
    account_a=random_info()
    account_b=random_info()
    
    while should_continue:
        account_a=account_b
        account_b=random_info()
        
        while account_a == account_b:
            account_b = random_info()

            print(f"Compare A: {get_info(account_a)}.")
            print(vs)
            print(f"Against B: {get_info(account_b)}.")    
            
            guess = input("Who has more followers? Type 'A' or 'B': ").lower()
            a_follower_count = account_a["follower_count"]
            b_follower_count = account_b["follower_count"]
            is_correct = num_check(guess, a_follower_count, b_follower_count)
            
            
            clear()
            print(logo)
            if is_correct:
                score += 1
                print(f"You're right! Current score: {score}.")
            else:
                should_continue = False
                print(f"Sorry, that's wrong. Final score: {score}")        
    
get_start()    
    


## 개선해야 할 점##
#  1.함수를 아래와 같이 받을 수 있음을 활용 
# -> return f' {name}, a {description}, from {country}.'

#  2.작게 작게 기획은 훌륭하였으나   score=0 을 넣지 않아 오류가 발생
# -> local variable 'score' referenced before assignment 

# 3. random_info() 랜덤으로 데이터 나오는 것을 변수로 저장하기 미흡
# -> account_a=random_info()