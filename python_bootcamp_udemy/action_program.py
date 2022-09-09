from replit import clear
#HINT: You can call clear() to clear the output in the console.

# from art import logo
# print(logo)
price_list={}

# flag 변수
bidding_finished=False # 기본값


# 가장 높은 가격 알려주는 함수 작성
def find_highest_bidder(bidding_reocord):
    highest_bid=0
    winner=''
    for bidder in bidding_reocord:
        bid_amount=bidding_reocord[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount    
            winner=bidder
    print(f'낙찰된 사람은 {winner}이고 가격은${highest_bid}')

# 이름과 입찰가 반복
while not bidding_finished:
    name=input("What is your name?: ")
    price=int(input("What is your bid?: $"))
    # 딕셔너리에 항목을 추가하기 위해 key:name, value:price
    price_list[name]=price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n") 
    if should_continue == "no":
        bidding_finished=True # while 반복문 종료
        find_highest_bidder(price_list)
    elif should_continue == "yes":
        clear()