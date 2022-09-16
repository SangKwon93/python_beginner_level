import random
from replit import clear

# 카드 랜덤 뽑기 
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card =random.choice(cards) 
    return card 

# 카드 리스트를 가지고 와서 카드로부터 계산된 점수를 반환
def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    return sum(cards)
    mask = 11 in cards and sum(cards) > 21
    if mask:    
        cards.append(11)
        cards.remove(1)

# 나와 컴퓨터 숫자 비교
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score ==0:
        return "Lose"
    elif user_score ==0:
        return "Lose"
    elif user_score >21:
        return "You went over. Lose"
    elif computer_score >21:
        return "Opponent went over. Win"
    elif user_score > computer_score:
        return "Yon Win"
    else:
        return "You Lose"    
        
# 카드 한장씩 더 가져가기
def play_game():
    

    user_cards=[]
    computer_cards=[]

    is_game_over=False
    for i in range(2):
        # new_card=deal_card()
        # user_cards.append(new_card) # new_card가 리스트인 경우에는 +- 사용가능 / 지금은 list 형식이기에 append
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not is_game_over:
        
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)

        print(f"너에 카드는 {user_cards} 이다.\n 현재 점수 {user_score}이다.")
        print(f"컴퓨터 카드는 {computer_cards[0]}이다.")

        if user_score==0 and computer_score ==0 or user_score> 21:
            is_game_over=True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass:")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else :
                is_game_over=True 

    while computer_score !=0 and computer_score <17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)
    
    
    print(f"나의 최종 숫자들 : {user_cards}, 나의 최종 점수 :{user_score}")
    print(f"컴퓨터의 최종 숫자들 : {computer_cards}, 컴퓨터 최종 점수 :{computer_score}")
    
        
    print(compare(user_score,computer_score))


# 반복하면서 재 시작        
while input("Do you want to play a game of Blackjack? Type 'y' or'n':") == "y":
    clear()
    play_game()
    

    
    
    
    
    
    
    
    
    
# calculate_score(user_cards)

# q1 = input("Do you want to play a game of Blackjack ? Type 'y' or 'n':")
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# if q1 == 'y':
    
#     your_card = [random.choice(cards) for i in range(2)]
#     computer_first = random.choice(cards)
#     print(f"너에 카드는 {your_card}\n컴퓨터의 첫번째 카드는 {computer_first} 이다.")
# else:
#     print("게임 종료")
    

# q2 = input("Type 'y' to get card, type 'n' to pass:")
# if q2 == 'n':
#     print(f"너에 카드는 {your_card} 이다.")
#     computer_secound = random.choice(cards)
#     computer_card=[computer_first,computer_secound]
#     print(f"컴퓨터 카드는 {computer_card}이다.")
#     if sum(your_card) > 21:
#         print("너는 졌어")
#     elif sum(your_card) > sum(computer_card):
#         print("너가 이겼다.")
#     else:
#         print("컴퓨터가 이겼다.")
    
